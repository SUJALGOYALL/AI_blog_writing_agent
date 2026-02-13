from pathlib import Path
from langgraph.graph import StateGraph, START, END
from schemas import State, GlobalImagePlan
from prompts import DECIDE_IMAGES_SYSTEM
from config import llm
from services.image_gen import generate_image_bytes
from langchain_core.messages import SystemMessage, HumanMessage


def merge_content(state: State) -> dict:
    body = "\n\n".join(md for _, md in sorted(state["sections"]))
    return {"merged_md": f"# {state['plan'].blog_title}\n\n{body}"}


def decide_images(state: State) -> dict:
    planner = llm.with_structured_output(GlobalImagePlan)
    plan = planner.invoke(
        [
            SystemMessage(content=DECIDE_IMAGES_SYSTEM),
            HumanMessage(content=state["merged_md"]),
        ]
    )
    return {
        "md_with_placeholders": plan.md_with_placeholders,
        "image_specs": [img.model_dump() for img in plan.images],
    }


def generate_and_place_images(state: State) -> dict:
    md = state["md_with_placeholders"]
    images_dir = Path("images")
    images_dir.mkdir(exist_ok=True)

    for spec in state["image_specs"]:
        img = generate_image_bytes(spec["prompt"])
        (images_dir / spec["filename"]).write_bytes(img)

        md = md.replace(
            spec["placeholder"],
            f"![{spec['alt']}](images/{spec['filename']})\n*{spec['caption']}*",
        )

    return {"final": md}


reducer_graph = StateGraph(State)
reducer_graph.add_node("merge", merge_content)
reducer_graph.add_node("images", decide_images)
reducer_graph.add_node("generate", generate_and_place_images)
reducer_graph.add_edge(START, "merge")
reducer_graph.add_edge("merge", "images")
reducer_graph.add_edge("images", "generate")
reducer_graph.add_edge("generate", END)

reducer_subgraph = reducer_graph.compile()

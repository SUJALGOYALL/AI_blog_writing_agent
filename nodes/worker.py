from langchain_core.messages import SystemMessage, HumanMessage
from schemas import Task, Plan
from prompts import WORKER_SYSTEM
from config import llm


def worker_node(payload: dict) -> dict:
    task = Task(**payload["task"])
    section_md = llm.invoke(
        [
            SystemMessage(content=WORKER_SYSTEM),
            HumanMessage(content=f"Section title: {task.title}"),
        ]
    ).content.strip()

    return {"sections": [(task.id, section_md)]}

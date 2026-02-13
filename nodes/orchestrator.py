from langchain_core.messages import SystemMessage, HumanMessage
from schemas import State, Plan
from prompts import ORCH_SYSTEM
from config import llm


def orchestrator_node(state: State) -> dict:
    planner = llm.with_structured_output(Plan)
    plan = planner.invoke(
        [
            SystemMessage(content=ORCH_SYSTEM),
            HumanMessage(content=f"Topic: {state['topic']}"),
        ]
    )
    return {"plan": plan}

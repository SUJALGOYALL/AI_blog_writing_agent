from langchain_core.messages import SystemMessage, HumanMessage
from config import llm
from schemas import State, RouterDecision
from prompts import ROUTER_SYSTEM


def router_node(state: State) -> dict:
    decider = llm.with_structured_output(RouterDecision)
    decision = decider.invoke(
        [
            SystemMessage(content=ROUTER_SYSTEM),
            HumanMessage(content=f"Topic: {state['topic']}"),
        ]
    )
    return decision.model_dump()

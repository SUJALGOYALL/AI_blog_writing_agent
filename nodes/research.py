from langchain_core.messages import SystemMessage, HumanMessage
from schemas import State, EvidencePack
from prompts import RESEARCH_SYSTEM
from config import llm
from services.tavily import tavily_search


def research_node(state: State) -> dict:
    raw = []
    for q in state.get("queries", []):
        raw.extend(tavily_search(q))

    if not raw:
        return {"evidence": []}

    extractor = llm.with_structured_output(EvidencePack)
    pack = extractor.invoke(
        [
            SystemMessage(content=RESEARCH_SYSTEM),
            HumanMessage(content=f"Raw results:\n{raw}"),
        ]
    )

    dedup = {e.url: e for e in pack.evidence if e.url}
    return {"evidence": list(dedup.values())}

from langgraph.graph import END, START, StateGraph

from .nodes.nodes import extract_skill, get_jd, get_resume, rate_resume
from .state import ResumeState

builder = StateGraph(ResumeState)
builder.add_node("get_jd", get_jd)
builder.add_node("extract_skills", extract_skill)
builder.add_node("get_resume", get_resume)
builder.add_node("rate_resume", rate_resume)

# fan-out: JD branch and resume branch run in parallel
builder.add_edge(START, "get_jd")
# builder.add_edge(START, "parse_resume")
builder.add_edge("get_jd", "extract_skills")
builder.add_edge("get_jd", "get_resume")
# join: rate_resume waits for BOTH branches
builder.add_edge(["extract_skills", "get_resume"], "rate_resume")
builder.add_edge("rate_resume", END)

graph = builder.compile()

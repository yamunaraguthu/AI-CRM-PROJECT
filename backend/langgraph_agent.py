from langgraph.graph import StateGraph
from typing import TypedDict
from tools import log_interaction
from agent import summarize_text

class State(TypedDict):
    doctor_name: str
    date: str
    notes: str
    summary: str

# Step function
def process(state: State):
    summary = summarize_text(state["notes"])
    state["summary"] = summary

    log_interaction(state)

    return state

# Build graph
builder = StateGraph(State)
builder.add_node("process", process)
builder.set_entry_point("process")

graph = builder.compile()
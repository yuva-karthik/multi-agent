from typing import Annotated, TypedDict

from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages

from agents.yellow import yellow_agent
from agents.black import black_agent
from agents.blue import blue_agent


class AgentState(TypedDict):
    topic: str
    messages: Annotated[list, add_messages]
    iteration: int


# Create graph
graph = StateGraph(AgentState)


# Add agents
graph.add_node("yellow", yellow_agent)
graph.add_node("black", black_agent)
graph.add_node("blue", blue_agent)


# Node to increment iteration count
def increment_iteration(state: AgentState):
    return {
        "iteration": state["iteration"] + 1
    }


graph.add_node("increment", increment_iteration)


# Initial flow
graph.add_edge(START, "yellow")

graph.add_edge("yellow", "black")

graph.add_edge("black", "blue")

graph.add_edge("blue", "increment")


# Decide whether to continue or stop
def should_continue(state: AgentState):
    if state["iteration"] < 2:
        return "yellow"

    return END


# Conditional loop
graph.add_conditional_edges(
    "increment",
    should_continue,
    {
        "yellow": "yellow",
        END: END
    }
)


# Compile graph
app = graph.compile()


# Run graph
if __name__ == "__main__":

    initial_state = {
        "topic": "does pineapple belong on pizza?",
        "messages": [],
        "iteration": 0
    }

    result = app.invoke(initial_state)

    print("\n========== DISCUSSION ==========\n")

    for msg in result["messages"]:
        print(f"{msg.name}:")
        print(msg.content)
        print()
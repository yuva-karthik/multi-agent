from typing import Annotated , TypedDict

from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages

from agents.yellow import yellow_agent
from agents.black import black_agent
from agents.blue import blue_agent

class AgentState(TypedDict):
    topic: str
    messages: Annotated[list, add_messages]

graph = StateGraph(AgentState)

graph.add_node("yellow",yellow_agent)
graph.add_node("black",black_agent)
graph.add_node("blue",blue_agent)

graph.add_edge(START,"yellow")
graph.add_edge("yellow","black")
graph.add_edge("black","blue")
graph.add_edge("blue",END)

app = graph.compile()

if __name__ == "__main__":
    initial_state = {
        "topic" : "does pineapple belong on pizza?",
        "messages" : []
    }

    result = app.invoke(initial_state)
    print("\n ==========DISCUSSION========== \n")
    for msg in result["messages"]:
        print(f"{msg.name}:")
        print(msg.content)
        print()
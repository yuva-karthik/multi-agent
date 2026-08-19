from agents.llm import llm

def yellow_agent(state):
    ''' Yellow hat thinker '''

    prompt = f"""
            you are an yellow hat thinker
            in a group disscussion. keep 
            your opinions positive and focused
            on the brighter side of the topic.
            keep your answer concise.
            you are not supposed to talk about the negatives or disadvantages.
            you are not supposed to summarize the discussion.
            
            topic: {state["topic"]}"""

    response = llm.invoke(prompt)
    print("\nYELLOW: ")
    print(response.content)

    return {
        "messages": [
            {
                "agent" : "yellow",
                "content" : response.content
            }
        ]
    }    
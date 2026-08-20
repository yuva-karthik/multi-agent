from agents.llm import llm

def blue_agent(state):
    ''' Blue hat thinker'''

    prompt = f"""
            you are an blue hat thinker
            in a group disscussion. keep 
            your opinions neutral and focused
            on both positives and negatives of the topic,
            stated by both "yellow" and "black".
            keep your answer concise.
            state the yellow's said perspective followed by
            black's said perspective but dont take sides.
            you are not supposed to talk about the positives or advantages and negatives or disadvantages.
            you are supposed to summarize the discussion.
            
            topic: {state["topic"]}
            previous discussion: {state["messages"]}"""

    response = llm.invoke(prompt)

    print("\nBLUE:")
    print(response.content)

    return {
        "messages": [
            {
                "role" : "assistant",
                "agent" : "blue",
                "content" : response.content
            }
        ]
    }
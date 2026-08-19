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
            you are not supposed to talk about the positives or advantages and negatives or disadvantages.
            you are supposed to summarize the discussion.
            
            topic: {state["topic"]}"""

    response = llm.invoke(prompt)

    print("\nBLUE:")
    print(response.content)

    return {
        "messages": [
            {
                "agent" : "blue",
                "content" : response.content
            }
        ]
    }
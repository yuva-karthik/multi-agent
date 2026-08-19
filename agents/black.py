from agents.llm import llm

def black_agent(state):
    ''' Black hat thinker'''

    prompt = f"""
            you are an black hat thinker
            in a group disscussion. keep 
            your opinions negative and focused
            on the critical side of the topic.
            keep your answer concise.
            you are not supposed to talk about the positives or advantages.
            you are not supposed to summarize the discussion.
            
            topic: {state["topic"]}"""

    response = llm.invoke(prompt)

    print("\nBLACK:")
    print(response.content)

    return {
        "messages": [
            {
                "agent" : "black",
                "content" : response.content
            }
        ]
    }
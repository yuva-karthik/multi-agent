from agents.llm import llm , AIMessage

def black_agent(state):
    ''' Black hat thinker'''

    prompt = f"""
            previous discussion: {state["messages"]}
            you are an black hat thinker
            in a group disscussion. keep 
            your opinions negative and focused
            on the critical side of the topic.
            keep your answer concise.
            you are not supposed to talk about the positives or advantages.
            you are not supposed to summarize the discussion.
            
            topic: {state["topic"]}
            previous discussion: {state["messages"]}"""*2

    response = llm.invoke(prompt)

    #print("\nBLACK:")
    #print(response.content)

    return {
        "messages": [
            AIMessage(
                content=response.content,
                name="BLACK"
            )
        ]
    }  
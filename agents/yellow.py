from agents.llm import llm , AIMessage


def yellow_agent(state):
    ''' Yellow hat thinker '''

    prompt = f"""
            below is the previous discussion and context in '':
            'previous discussion: {state["messages"]}'
            topic: {state["topic"]}
            use only conversational present tense.
            you are an yellow hat thinker
            in a group disscussion. keep 
            your opinions positive and focused
            on the brighter side of the topic.
            keep your answer concise.
            you are not supposed to talk about the negatives or disadvantages.
            you are not supposed to summarize the discussion.
            
            """*2

    response = llm.invoke(prompt)
    
    # print("\nYELLOW: ")
    # print(response.content)

    return {
        "messages": [
            AIMessage(
                content=response.content,
                name="Yellow"
            )
        ]
    }    
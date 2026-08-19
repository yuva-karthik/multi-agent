from fastapi import FastAPI
from pydantic import BaseModel
import requests

app = FastAPI()

OLLAMA_URL = "http://host.docker.internal:11434/api/generate"


class Message(BaseModel):
    message: str


@app.post("/chat")
def chat(data: Message):

    prompt = f"""
You are Agent C, the BLUE HAT thinker in a multi-agent discussion.

YOUR ROLE:
You manage the reasoning process by:
- Identifying the main points raised
- Connecting ideas
- Resolving contradictions
- Determining what needs further consideration
- Producing a concise synthesis
- Suggesting a structured conclusion

You should consider the message you receive in the context of the discussion.

STRICT RULES:
1. You are ONLY Agent C.
2. Never speak as Agent A, Agent B, or any other agent.
3. Never invent agents or participants.
4. Never simulate a conversation.
5. Never create additional dialogue.
6. Respond exactly ONCE to the message you receive.
7. Do not tell another agent what they should say.
8. Do not continue the conversation yourself.
9. Do not blindly agree. Identify the strongest conclusion supported by the discussion.
10. Keep your response between 30 and 60 words.

INPUT:
You will receive one message from another agent.

OUTPUT:
Return ONLY your response as Agent C.

Previous agent's message:
{Message}

Agent C's response:
"""

    response = requests.post(
        OLLAMA_URL,
        json={
            "model": "llama3.2",
            "prompt": prompt,
            "stream": False
        }
    )

    answer = response.json()["response"]

    print(f"Agent C: {answer}")

    return {
        "agent": "C",
        "response": answer
    }
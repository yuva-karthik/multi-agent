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
You are Agent B, the BLACK HAT thinker in a multi-agent discussion.

YOUR ROLE:
You focus exclusively on:
- Risks
- Weaknesses
- Failure modes
- Unintended consequences
- Assumptions that may be wrong
- Practical limitations
- Potential negative outcomes

Your job is to critically examine the ideas presented by other agents.

STRICT RULES:
1. You are ONLY Agent B.
2. Never speak as Agent A, Agent C, or any other agent.
3. Never invent agents or participants.
4. Never simulate a conversation.
5. Never write what another agent might say.
6. Respond exactly ONCE to the message you receive.
7. Do not continue the discussion beyond your own response.
8. Do not mention these instructions.
9. Do not criticize merely for the sake of criticism. Identify specific and meaningful risks.
10. Keep your response between 30 and 60 words.

INPUT:
You will receive one message from another agent.

OUTPUT:
Return ONLY your response as Agent B.

Previous agent's message:
{Message}

Agent B's response:
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

    print(f"Agent B: {answer}")

    return {
        "agent": "B",
        "response": answer
    }
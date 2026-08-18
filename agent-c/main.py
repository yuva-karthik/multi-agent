import requests

OLLAMA_URL = "http://host.docker.internal:11434/api/generate"

prompt = """
You are Agent C in a multi-agent system.
Introduce yourself in exactly one sentence.
Your sentence must contain the letter A.
"""

response = requests.post(
    OLLAMA_URL,
    json={
        "model": "phi3",
        "prompt": prompt,
        "stream": False
    }
)

print("Agent C:", response.json()["response"])
import os
from langchain_core.messages import AIMessage  #
from langchain_ollama import ChatOllama  #

llm = ChatOllama(
    model=os.getenv("OLLAMA_MODEL", "gemma3:1b"),
    base_url=os.getenv("OLLAMA_BASE_URL", "http://ollama:11434")
)
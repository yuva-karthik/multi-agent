from langchain_ollama import ChatOllama

llm = ChatOllama(model="llama3.2",
                 base_url="http://host.docker.internal:11434")
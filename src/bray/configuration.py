import os
from dotenv import load_dotenv

load_dotenv()

OLLAMA_HOST = os.getenv('OLLAMA_HOST')
CHROMA_HOST = os.getenv('CHROMA_HOST')
CHROMA_PORT = os.getenv('CHROMA_PORT')
EMBEDDING_MODEL = os.getenv('EMBEDDING_MODEL')
LLM_MODEL = os.getenv('LLM_MODEL')

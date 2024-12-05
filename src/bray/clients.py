import chromadb
import ollama
import configuration

chroma = chromadb.HttpClient(host=configuration.CHROMA_HOST,
                             port=configuration.CHROMA_PORT,
                             settings=chromadb.Settings(allow_reset=True, anonymized_telemetry=False))

ollama = ollama.Client(host=configuration.OLLAMA_HOST)

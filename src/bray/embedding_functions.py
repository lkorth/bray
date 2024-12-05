import clients
import configuration

def store(directory_hash, files):
    collection = clients.chroma.create_collection(name=directory_hash)

    for i, file in enumerate(files):
        for i2, d in enumerate(file):
          response = clients.ollama.embeddings(model=configuration.EMBEDDING_MODEL, prompt=d)
          embedding = response["embedding"]
          collection.add(ids=[str(i) + str(i2)], embeddings=[embedding], documents=[d])

import clients
import configuration

def retrieve(directory_hash, prompt):
    embedding_response = clients.ollama.embeddings(prompt=prompt, model=configuration.EMBEDDING_MODEL)

    collection = clients.chroma.get_collection(name=directory_hash)
    results = collection.query(query_embeddings=[embedding_response["embedding"]], n_results=3)

    return results['documents'][0][0]

def generate_with_context(data, prompt):
    output = clients.ollama.generate(
        model=configuration.LLM_MODEL,
        prompt=f"Using this data: {data}. Respond to this prompt: {prompt}"
    )

    return output['response']

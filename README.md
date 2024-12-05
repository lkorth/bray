# Bray

BRAY - Baseline Rag Ai analYsis

## What is RAG?

RAG stands for Retrieval-Augmented Generation, which is a natural language processing (NLP) technique that combines
generative and retrieval-based artificial intelligence (AI) models. RAG helps generate more relevant, accurate, and
up-to-date responses.

## Technologies

Bray runs on top of the [Ollama framework](https://ollama.com/) and utilizes [Chroma](https://www.trychroma.com/) as a vector
database for embeddings.

Bray can be configured to use any embedding and LLM via the [.env file](.env).

## Usage

Start the services in Docker

```bash
docker-compose up -d
```

Pull the required models

```bash
docker exec -it ollama ollama pull nomic-embed-text
docker exec -it ollama ollama pull llama3.2:1b
```

Create embeddings for markdown files

```bash
python3 src/bray/bray.py load
```

Execute a prompt utilizing embeddings

```bash
python3 src/bray/bray.py retrieve
```
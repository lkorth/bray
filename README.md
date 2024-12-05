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

Install dependencies

```bash
python3 -m pip install -r requirements.txt
```

Create embeddings for markdown files in the current directory

```bash
python3 PATH_TO_BRAY/src/bray/bray.py load
```

Execute a prompt utilizing embeddings for markdown files in the current directory

```bash
python3 PATH_TO_BRAY/src/bray/bray.py retrieve
```

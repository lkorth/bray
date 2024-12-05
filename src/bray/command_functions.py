import os
import hashlib
import file_functions
import embedding_functions
import retrieval_functions

def md5(data):
  if isinstance(data, str):
    data = data.encode()

  return hashlib.md5(data).hexdigest()

def load():
    directory_path = os.getcwd()
    file_type = "md"
    files = file_functions.get_files_by_type(directory_path, file_type)

    documents = []
    for file in files:
        documents.append(file_functions.chunk_markdown_file(file))

    embedding_functions.store(md5(directory_path), documents)

def retrieve():
    prompt = input("Enter your question: ")
    directory_path = os.getcwd()
    data = retrieval_functions.retrieve(md5(directory_path), prompt)

    print(retrieval_functions.generate_with_context(data, prompt))

import os
import glob

def get_files_by_type(directory, file_type):
    return glob.glob(os.path.join(directory, f"**/*.{file_type}"), recursive=True)

def chunk_markdown_file(filename):
    with open(filename, 'r') as file:
        groups = []
        current_group = ""

        for line in file:
          line = line.strip()
          if line.startswith("#"):
            if current_group:
              groups.append(current_group)
              current_group = ""
          current_group += line + " "

        if current_group:
          groups.append(current_group)

        return groups

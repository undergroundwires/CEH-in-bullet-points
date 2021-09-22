import re
import mkdocs_gen_files

# Move the "README.md" file into chapters/, for use by MkDocs.
with open("README.md") as in_f, mkdocs_gen_files.open("README.md", "w") as out_f:
    for line in in_f:
        line = re.sub(r'\bchapters/', '', line)
        # Replace 3-space indentation in lists with 4-space indentation:
        line = re.sub(r'^ ?( +)\1\1\b', r'\1\1\1\1', line)
        out_f.write(line)

# Moves the "README.md" file into chapters/, for use by MkDocs.

import re
import mkdocs_gen_files

with open("README.md") as in_f, mkdocs_gen_files.open("README.md", "w") as out_f:
    for line in in_f:
        out_f.write(re.sub(r'\bchapters/', '', line))

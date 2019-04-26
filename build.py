import subprocess
import json

with open(".zenodo.json", 'r') as f:
    zenodo = json.load(f)

print(zenodo)

root = [
    "pandoc",
    "manuscript.md"
]

common_flags = [
    "--filter", "pandoc-fignos",
    "--filter", "pandoc-eqnos",
    "--filter", "pandoc-tablenos",
    "--filter", "pandoc-citeproc",
    "--bibliography=references.json",
    "--metadata-file=.zenodo.json"
]

# Version for the website
subprocess.run(root + ["-o", "index.html", "--template", "templates/index.html"] + common_flags)

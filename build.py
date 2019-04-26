import subprocess
import json
import logging

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

versions = {
    "Website index": ["-o", "index.html", "--template", "barlock/templates/index.html", "--webtex"],
    "PDF document": ["-o", "manuscript.pdf"]
}

for version in versions:
    logging.info(version)
    subprocess.run(root + versions[version]  + common_flags)

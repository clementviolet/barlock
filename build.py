import subprocess
import json

with open(".zenodo.json", 'r') as f:
    zenodo = json.load(f)

filename = "_".join(zenodo["title"].split()[:6])

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
    "--metadata-file=.zenodo.json",
    "--variable=filename:" + filename
]

versions = {
    "Website index": ["-o", "index.html", "--template", "barlock/templates/index.html", "--webtex"],
    "PDF document": ["-o", filename + ".pdf"],
    "TEX source": ["-o", filename + ".tex"]
}

for version in versions:
    print(version)
    subprocess.run(root + versions[version]  + common_flags)

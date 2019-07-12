import subprocess
import json
import os

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

current_branch = os.getenv('BRANCH', 'master')
if current_branch == "master":
    dest = "."
else:
    dest = "./" + current_branch
print(current_branch)

versions = {
    "Website index": ["-o", dest+"/"+"index.html", "--template", "barlock/templates/index.html", "--webtex"],
    "PDF document": ["-o", dest + "/" + filename + ".pdf"],
    "TEX source": ["-o", dest + "/" + filename + ".tex"],
    "MS Word": ["-o", dest + "/" + filename + ".docx"]
}

for version in versions:
    print(version)
    print(versions[version])
    subprocess.run(root + versions[version]  + common_flags)

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
        "--csl", "barlock/plab.csl",
        "--metadata-file=.zenodo.json",
        "--variable=filename:" + filename
        ]

versions = {
        "index.html": ["--template", "barlock/templates/index.html", "--webtex"],
        filename + ".pdf": ["--pdf-engine=lualatex"],
        filename + ".tex": [],
        filename + ".docx": []
        }

current_branch = os.getenv('TRAVIS_BRANCH', 'master')
print("building on branch " + current_branch)
if (current_branch != "master"):
    subprocess.run(["mkdir", "-p", current_branch])
    subprocess.run(["cp", "-r", "figures", current_branch])

subprocess.run(["cp", "-r", "barlock/assets", "."])

for version in versions:
    print(version)
    subprocess.run(root + ["-o", version] + versions[version] + common_flags)
    if current_branch != "master":
        subprocess.run(["mv", version, current_branch + "/" + version])

# Clean the biobliography
with open("references.json") as jsfile:
    references = json.load(jsfile)

# Fields to remove
fields = ["source", "abstract", "language", "accessed", "container-title-short", "title-short", "ISSN"]
for reference in references:
    for field in fields:
        reference.pop(field, None)

with open("references.json", "w") as outfile:
    json.dump(references, outfile, sort_keys=True, indent=4, separators=(',', ': '))
    outfile.write('\n')
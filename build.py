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

    subprocess.run("mkdir" + "-p" + current_branch)
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
    "index.html": ["--template", "barlock/templates/index.html", "--webtex"],
    filename + ".pdf": [],
    filename + ".tex": [],
    filename + ".docx": []
}

current_branch = os.getenv('TRAVIS_BRANCH', 'master')
if current_branch != "master":
    subprocess.run("mkdir" + "-p" + current_branch)

print("BUILD FOR " + current_branch)

for version in versions:
    print(version)
    print(versions[version])
    subprocess.run(root + ["-o", version] + versions[version] + common_flags)
    subprocess.run("mv" + version + current_branch)

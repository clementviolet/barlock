import subprocess
import json

subprocess.run["ls", "-l"]

with open(".zenodo.json", 'r') as f:
    zenodo = json.load(f)

print(zenodo)

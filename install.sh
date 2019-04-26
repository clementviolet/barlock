#! /bin/bash

wget https://github.com/jgm/pandoc/releases/download/2.7.2/pandoc-2.7.2-1-amd64.deb
sudo dpkg -i pandoc-2.7.2-1-amd64.deb

sudo apt-get install pandoc-citeproc -y

pip install -r barlock/requirements.txt

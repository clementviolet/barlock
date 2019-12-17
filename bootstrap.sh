#! /bin/bash

sudo apt-get update

# Fonts
sudo apt-get install fonts-lato

# TinyTeX
wget -qO- "https://yihui.name/gh/tinytex/tools/install-unx.sh" | sh
tlmgr install xcolor
tlmgr install mdwtools
tlmgr install amsfonts
tlmgr install setspace

# XeTeX
tlmgr install unicode-math
tlmgr install polyglossia

# Pandoc 2.7.2
wget https://github.com/jgm/pandoc/releases/download/2.7.3/pandoc-2.7.3-1-amd64.deb
sudo dpkg -i pandoc-2.7.3-1-amd64.deb
rm pandoc-2.7.3-1-amd64.deb

# Python requirements (pandoc filters)
pip install -r barlock/requirements.txt

# Convert .bib file  to .json
pandoc-citeproc --bib2json references.bib > references.json
#! /bin/bash

# TinyTeX
#wget -qO- "https://yihui.name/gh/tinytex/tools/install-unx.sh" | sh
# sudo apt-get install tex-common
# sudo apt-get install texlive-base
# sudo apt-get install texlive-binaries
# sudo apt-get install texlive-luatex
# sudo apt-get install texlive-luatex
# sudo apt-get install texlive-full
# tlmgr install xcolor
# tlmgr install mdwtools
# tlmgr install amsfonts
# ###
# tlmgr install unicode-math
# tlmgr install lualatex-math
# tlmgr install filehook
# tlmgr install lm-math # Font


# Pandoc 2.7.2
wget https://github.com/jgm/pandoc/releases/download/2.7.3/pandoc-2.7.3-1-amd64.deb
sudo dpkg -i pandoc-2.7.3-1-amd64.deb
rm pandoc-2.7.3-1-amd64.deb

# Python requirements (pandoc filters)
pip install -r barlock/requirements.txt

# Convert .bib file  to .json
pandoc-citeproc --bib2json references.bib > references.json
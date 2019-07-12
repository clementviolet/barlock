#! /bin/bash

export BRANCH=$(if [ "$TRAVIS_PULL_REQUEST" == "false" ]; then echo $TRAVIS_BRANCH; else echo $TRAVIS_PULL_REQUEST_BRANCH; fi)

# TinyTeX
wget -qO- "https://yihui.name/gh/tinytex/tools/install-unx.sh" | sh
tlmgr install xcolor
tlmgr install mdwtools

# Pandoc 2.7.2
wget https://github.com/jgm/pandoc/releases/download/2.7.2/pandoc-2.7.2-1-amd64.deb
sudo dpkg -i pandoc-2.7.2-1-amd64.deb
rm pandoc-2.7.2-1-amd64.deb

# Python requirements (pandoc filters)
pip install -r barlock/requirements.txt

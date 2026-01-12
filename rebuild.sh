#! /usr/bin/bash

if [ ! -d .venv ]
then
    python3 -m venv .venv
fi

source .venv/bin/activate
pip install jinja2 pyyaml pygvariant
./build_modules.sh
ansible-galaxy collection install . --force
./build_docs.sh


#!/bin/bash
virtualenv -p python3 venv
./activate-linux.sh
pip3 install -r requirements.txt
deactivate
#!/bin/bash
py -3.6 -m venv venv
. ./venv/bin/activate
pip install --upgrade pip
pip install --upgrade setuptools
pip install -r requirements.txt
deactivate
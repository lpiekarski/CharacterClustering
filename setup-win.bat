@echo off
python -m venv venv
.\activate-win.bat
pip install -r requirements.txt
deactivate
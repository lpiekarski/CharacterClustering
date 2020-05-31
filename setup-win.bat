py -3 -m venv venv
CALL .\venv\Scripts\activate.bat
python -m pip install --upgrade pip
python -m pip install --upgrade setuptools
python -m pip install -r requirements.txt
deactivate
#!/bin/bash
echo "Creating virtual environment"
python3.8 -m venv venv
if [ $? -ne 0 ]; then
  echo "ERROR: could not create virtual environment"
  exit 3
fi

. venv/bin/activate

pip install --upgrade pip
pip install -r requirements.txt
python src/main.py
/usr/bin/open http://127.0.0.1:5000/swagger
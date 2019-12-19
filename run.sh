#!/bin/bash

if [ ! -d venv ]; then
    echo "... creating virtual environment"
    python -m venv venv
fi

echo "... starting virtual environment"
source venv/bin/activate

echo "... installing requirements"
# pip install --upgrade pip
pip install -q -r requirements.txt

echo "... runnning main.py"
python main.py
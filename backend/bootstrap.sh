#!/bin/bash
export FLASK_APP=./src/main.py
export FLASK_ENV=development
export FLASK_DEBUG=true
source activate rw-angular
flask run -h 0.0.0.0

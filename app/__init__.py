# usage:
# Activate virtual environment 
# $ . venv/.venv/bin/activate
# $ pip install -r requirements.txt
# $ cd app
# $ export FLASK_APP=__init__.py
# $ export FLASK_ENV=development
# $ flask run
# quit deploy
# $ ctrl c 
# deactivates venv 
# $ deactivate 

from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"
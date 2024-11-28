# usage: 
# $ . venv/.venv/bin/activate
# $ pip install requirements.txt
# $ cd app
# $ flask --app __init__ run
# quit deploy
# $ ctl c 
# deactivates venv 
# $ deactivate 

from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"
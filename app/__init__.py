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

from flask import Flask, request, g, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
from flask_babel import Babel, _

app = Flask(__name__)

# Babel configuration
app.config['BABEL_DEFAULT_LOCALE'] = 'en' # default language
app.config['BABEL_SUPPORTED_LOCALES'] = ['en', 'es', 'fr'] # languages supported
app.config['BABEL_TRANSLATION_DIRECTORIES'] = "../translations" # directory with translations

def get_locale():
    return request.accept_languages.best_match(['en', 'es', 'fr'])

# Initialize extensions
"""You can add other extensions here, e.g. db = SQLAlchemy(app)"""
babel = Babel(app, locale_selector=get_locale)


@app.route("/")
def hello_world():
    return _("Hello, World!")
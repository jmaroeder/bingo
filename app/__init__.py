from flask import Flask
from flask_bootstrap import Bootstrap
from .characters import CHARACTERS

app = Flask(__name__)
bootstrap = Bootstrap(app)


from . import routes

from flask import Flask
from flask_bootstrap import Bootstrap
from flask_talisman import Talisman


from .characters import CHARACTERS

app = Flask(__name__)
bootstrap = Bootstrap(app)
csp = {
    'default-src': '*'
}
Talisman(app, content_security_policy=csp)

from . import routes

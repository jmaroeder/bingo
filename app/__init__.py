from flask import Flask
from flask_bootstrap import Bootstrap
from flask_cachebuster import CacheBuster
from flask_talisman import Talisman

from .characters import CHARACTERS

app = Flask(__name__)
bootstrap = Bootstrap(app)
csp = {
    'default-src': '*'
}
cache_buster = CacheBuster(config={'extensions': ['.js', '.css', '.csv'], 'hash_size': 5})
cache_buster.init_app(app)
Talisman(app, content_security_policy=csp)

from . import routes

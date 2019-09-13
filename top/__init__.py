import os
from flask import Flask

top = Flask(__name__)
top.secret_key = os.urandom(16)

from top import routes

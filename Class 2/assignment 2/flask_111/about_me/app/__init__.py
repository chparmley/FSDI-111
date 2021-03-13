#!/user/bin/env python3
# -*- coding: utf8 -*-
"""Sample app"""

# From flask module import Flask Class
from flask import Flask
from flask_bootstrap import Bootstrap

# Create object form the Flask class with __name__ as it's parameter
app = Flask(__name__)

Bootstrap(app)

# from app module import routes routes.py file
from about_me.app import routes
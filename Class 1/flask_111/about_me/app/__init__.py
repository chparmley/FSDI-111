#!/user/bin/env python3
# -*- coding: utf8 -*-
"""Sample app"""

# From flask module import Flask Class
from flask import Flask

# Create object form the Flask class with __name__ as it's parameter
app = Flask(__name__)

# from app module import routes routes.py file
from about_me.app import routes
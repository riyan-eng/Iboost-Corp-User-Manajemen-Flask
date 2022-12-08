from .budget import *
from .wallet import *

from flask import render_template

def Transaction():
    return render_template("transaction/index.html")
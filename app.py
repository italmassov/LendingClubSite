from flask import Flask, render_template, request, redirect
import flask
import requests
import datetime
import pandas as pd
import numpy as np

from bokeh.embed import components
from bokeh.plotting import figure
from bokeh.resources import INLINE
from bokeh.templates import RESOURCES
from bokeh.utils import encode_utf8

app = Flask(__name__)

colors = {
    'Black': '#000000',
    'Red': '#FF0000',
    'Green': '#00FF00',
    'Blue': '#00FF00'
}

dates = 0
closing_prices = 0

# stock ticker
st = ''

def getitem(obj, item, default):
    if item not in obj:
        return default
    else:
        return obj[item]

@app.route('/')
def main():
  return redirect('/index')

@app.route('/index')
def index():
  return render_template('index.html')

if __name__ == '__main__':
  app.run(port=33507, debug=True)
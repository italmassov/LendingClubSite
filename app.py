from flask import Flask, render_template, request, redirect
import flask
import requests
import datetime

app = Flask(__name__)

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
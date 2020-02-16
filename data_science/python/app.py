import requests
from flask import Flask, render_template, request

app = Flask(__name__)
def index():
    return  render_template('index.html', gifs=gif_list)

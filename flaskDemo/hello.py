# coding=gbk

from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_word():
    return "<h1>hello, World</h1>"

# coding=gbk
from flask import Flask, render_template

app = Flask(__name__, template_folder="../templates", static_folder="")

@app.route('/')
def index():
    return render_template("hello.html")


if __name__ == '__main__':
    print("执行Hello模板解析！！！")
    app.run()
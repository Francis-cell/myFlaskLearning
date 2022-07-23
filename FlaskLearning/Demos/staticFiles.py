# coding=gbk

from flask import Flask, render_template

app = Flask(__name__, template_folder="../templates", static_folder="../staticFiles")


@app.route("/")
def index():
    return render_template("staticFiles.html")


if __name__ == '__main__':
    print("静态文件测试！！！")
    app.run()
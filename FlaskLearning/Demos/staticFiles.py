# coding=gbk

from flask import Flask, render_template

app = Flask(__name__, template_folder="../templates", static_folder="../staticFiles")


@app.route("/")
def index():
    return render_template("staticFiles.html")


if __name__ == '__main__':
    print("��̬�ļ����ԣ�����")
    app.run()
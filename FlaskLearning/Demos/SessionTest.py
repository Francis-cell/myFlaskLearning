# coding=gbk
from flask import Flask, session, request, redirect, url_for, render_template

app = Flask(__name__, template_folder="../templates")

# 设置应用程序的serect_key的值
app.secret_key = "xioieipcjmd3bfra2h"


@app.route("/")
def index():
    if 'username' in session:
        username = session['username']
        return '登录用户名是:' + username + '<br>' \
                "<b><a href = '/logout'>点击我退出登录</a></b>"
    return "您还没有登录，请先登录！！！<br>" \
            "<a href='/login'>点击此处进行登录</a>"


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        print("请求的时候，从form中接收到的数据为：", request.form)
        # 设置session会话的值
        session['username'] = request.form['username']
        return redirect(url_for('index'))
    return render_template("SessionTest.html")


@app.route("/logout")
def logout():
    # 移除session会话的值
    session.pop('username', None)
    return redirect(url_for('index'))


if __name__ == '__main__':
    print("会话测试！！！")
    app.run(debug=True)
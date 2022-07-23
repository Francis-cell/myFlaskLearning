# coding=gbk
from flask import Flask, request, redirect, url_for, render_template, abort

'''
    Flask.redirect(location, statuscode, response)
    1、location参数是应该重定向响应的URL。
    2、statuscode发送到浏览器标头，默认为302。
    3、response参数用于实例化响应。

    400 - 用于错误请求
    401 - 用于未身份验证的
    403 - Forbidden
    404 - 未找到
    406 - 表示不接受
    415 - 用于不支持的媒体类型
    429 - 请求过多
'''

app = Flask(__name__, template_folder="../templates")


@app.route("/")
def index():
    return render_template("SessionTest.html")


# @app.route("/login", methods=["GET", "POST"])
# def login():
#     if request.method == 'POST' and request.form['username'] == "admin":
#         return redirect(url_for('success'))
#     return redirect(url_for('index'))



@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == 'POST':
        if request.form['username'] == "admin":
            return redirect(url_for('success'))
        else:
            # 用于错误请求(在这种情况下：)
            abort(401)
    return redirect(url_for('index'))


@app.route("/success")
def success():
    return "登录成功！！！"


if __name__ == '__main__':
    print("重定向和错误！！！")
    app.run(debug=True)
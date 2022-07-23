# coding=gbk
from flask import Flask, render_template, request, flash, redirect, url_for

'''
    flash(message, category)
    1、message 参数是要闪现的实际消息。
    2、category 参数是可选的。它可以是“error”，“info”或“warning”。

从会话中删除消息
    get_flashed_messages(with_categories, category_filter)    
'''

app = Flask(__name__, template_folder="../templates", static_folder="../staticFiles")
app.secret_key = "n23ch1ahf9nwhki6t0"

@app.route("/")
def index():
    return render_template("messageFlash_Index.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    error = None
    if request.method == "POST":
        if request.form["username"] != "admin" or request.form["password"] != "admin":
            error = "账号或者密码不正确，请重新输入后再尝试！"
        else:
            flash("您已经成功登录！！！")
            return render_template("staticFiles.html")
    return render_template("login.html", error=error)



if __name__ == '__main__':
    print("消息闪现！！！")
    app.run(debug=True)
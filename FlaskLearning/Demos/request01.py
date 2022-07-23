# coding=gbk
from flask import Flask, redirect, url_for, request, render_template

app = Flask(__name__, template_folder="../html", static_folder="")

@app.route('/')
def index():
    return render_template('request01.html')

@app.route('/success/<name>')
def success(name):
    return 'welcome %s' % name

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        print('当前使用的是POST方法')
        # 对应的request01.html中的form表单，如果使用的是post请求的方式，那么将走这种方式
        user = request.form['nm']
        return redirect(url_for('success', name=user))
    else:
        print("当前使用的请求方式不是POST方式")
        # 对应的request01.html中的form表单，如果使用的是get请求的方式，那么将走这种方式
        user = request.args.get('nm')
        return redirect(url_for('success', name=user))


if __name__ == '__main__':
    app.run()
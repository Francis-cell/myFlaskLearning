# coding=gbk
from flask import Flask, session, request, redirect, url_for, render_template

app = Flask(__name__, template_folder="../templates")

# ����Ӧ�ó����serect_key��ֵ
app.secret_key = "xioieipcjmd3bfra2h"


@app.route("/")
def index():
    if 'username' in session:
        username = session['username']
        return '��¼�û�����:' + username + '<br>' \
                "<b><a href = '/logout'>������˳���¼</a></b>"
    return "����û�е�¼�����ȵ�¼������<br>" \
            "<a href='/login'>����˴����е�¼</a>"


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        print("�����ʱ�򣬴�form�н��յ�������Ϊ��", request.form)
        # ����session�Ự��ֵ
        session['username'] = request.form['username']
        return redirect(url_for('index'))
    return render_template("SessionTest.html")


@app.route("/logout")
def logout():
    # �Ƴ�session�Ự��ֵ
    session.pop('username', None)
    return redirect(url_for('index'))


if __name__ == '__main__':
    print("�Ự���ԣ�����")
    app.run(debug=True)
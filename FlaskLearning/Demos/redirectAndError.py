# coding=gbk
from flask import Flask, request, redirect, url_for, render_template, abort

'''
    Flask.redirect(location, statuscode, response)
    1��location������Ӧ���ض�����Ӧ��URL��
    2��statuscode���͵��������ͷ��Ĭ��Ϊ302��
    3��response��������ʵ������Ӧ��

    400 - ���ڴ�������
    401 - ����δ�����֤��
    403 - Forbidden
    404 - δ�ҵ�
    406 - ��ʾ������
    415 - ���ڲ�֧�ֵ�ý������
    429 - �������
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
            # ���ڴ�������(����������£�)
            abort(401)
    return redirect(url_for('index'))


@app.route("/success")
def success():
    return "��¼�ɹ�������"


if __name__ == '__main__':
    print("�ض���ʹ��󣡣���")
    app.run(debug=True)
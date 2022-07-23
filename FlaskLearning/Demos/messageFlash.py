# coding=gbk
from flask import Flask, render_template, request, flash, redirect, url_for

'''
    flash(message, category)
    1��message ������Ҫ���ֵ�ʵ����Ϣ��
    2��category �����ǿ�ѡ�ġ��������ǡ�error������info����warning����

�ӻỰ��ɾ����Ϣ
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
            error = "�˺Ż������벻��ȷ��������������ٳ��ԣ�"
        else:
            flash("���Ѿ��ɹ���¼������")
            return render_template("staticFiles.html")
    return render_template("login.html", error=error)



if __name__ == '__main__':
    print("��Ϣ���֣�����")
    app.run(debug=True)
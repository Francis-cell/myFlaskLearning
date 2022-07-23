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
        print('��ǰʹ�õ���POST����')
        # ��Ӧ��request01.html�е�form�������ʹ�õ���post����ķ�ʽ����ô�������ַ�ʽ
        user = request.form['nm']
        return redirect(url_for('success', name=user))
    else:
        print("��ǰʹ�õ�����ʽ����POST��ʽ")
        # ��Ӧ��request01.html�е�form�������ʹ�õ���get����ķ�ʽ����ô�������ַ�ʽ
        user = request.args.get('nm')
        return redirect(url_for('success', name=user))


if __name__ == '__main__':
    app.run()
# coding=gbk

# ����Flaskģ��
from flask import Flask
# �������htmlҳ���ģ��
from flask import render_template

# �½�һ��Flaskʵ��
'''
����˵����
    1��__name__: ��������
    2��template_folder: ָ��htmlҳ�����ڵ�·��
    3��static_folder: ָ����̬��Դ�ļ�(ͼƬ,bootStrap���ļ����ڵ�·��)
'''
app = Flask(__name__, template_folder="../html", static_folder="")

@app.route('/')
def login():
    # ����htmlģ��
    return render_template('login.html')


if __name__ == '__main__':
    app.run()
# coding=gbk
from flask import Flask
from flask_mail import Message, Mail

app = Flask(__name__, template_folder="../templates")
app.config['SECRET_KEY'] = 'ze0R3Gb#oW$X$gSHDOU$'

# ����Flask_Mail
app.config['MAIL_SERVER'] = "smtp.qq.com"
app.config['MAIL_PORT'] = 25
app.config['MAIL_USERNAME'] = "franciszmr@foxmail.com"
app.config['MAIL_PASSWORD'] = 'ueyqbfsvssozdahc'
app.config['MAIL_USE_TLS'] = True
mail = Mail(app)


@app.route("/")
def index():
    msg = Message(subject="Flask�ʼ����ԣ�", sender='franciszmr@foxmail.com', recipients=['zhumengren@sinosoft.com.cn'])
    msg.body = "����Flask�ʼ����ͣ�����---zmr"
    # �����ʼ�
    mail.send(msg)
    return "Sent"

if __name__ == '__main__':
    print("Flask �ʼ����ԣ�����")
    app.run(debug=True)
# coding=gbk
from flask import Flask
from flask_mail import Message, Mail

app = Flask(__name__, template_folder="../templates")
app.config['SECRET_KEY'] = 'ze0R3Gb#oW$X$gSHDOU$'

# 配置Flask_Mail
app.config['MAIL_SERVER'] = "smtp.qq.com"
app.config['MAIL_PORT'] = 25
app.config['MAIL_USERNAME'] = "franciszmr@foxmail.com"
app.config['MAIL_PASSWORD'] = 'ueyqbfsvssozdahc'
app.config['MAIL_USE_TLS'] = True
mail = Mail(app)


@app.route("/")
def index():
    msg = Message(subject="Flask邮件测试！", sender='franciszmr@foxmail.com', recipients=['zhumengren@sinosoft.com.cn'])
    msg.body = "测试Flask邮件发送！！！---zmr"
    # 发送邮件
    mail.send(msg)
    return "Sent"

if __name__ == '__main__':
    print("Flask 邮件测试！！！")
    app.run(debug=True)
# coding=gbk
'''
常见的WTform
1、TextField：表示<input type ='text'> HTML表单元素
2、BooleanField：表示<input type ='checkbox'> HTML表单元素
3、DecimalField：用于显示带小数的数字的文本字段
4、IntegerField：用于显示整数的文本字段
5、RadioField：表示<input type = 'radio'> HTML表单元素
6、SelectField：表示选择表单元素
7、TextAreaField：表示<textarea> HTML表单元素
8、PasswordField：表示<input type = 'password'> HTML表单元素
9、SubmitField：表示<input type = 'submit'>表单元素
'''

import pymysql
from flask import Flask, request
from wtforms import Form, BooleanField, StringField, PasswordField, validators

app = Flask(__name__)

# 注册一个登录表单类
class RegistrationForm(Form):
    user = StringField('userName', [validators.Length(min=4, max=25)])
    email = StringField('email', [validators.Length(min=6, max=25)])
    password = PasswordField('password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='密码必须一致！')
    ])
    confirm = PasswordField('请重复输入一遍密码！')
    accept_tos = BooleanField('接收登录！', [validators.DataRequired()])


# 定义一个User类
class User:
    def __init__(self, userName, email, password):
        self.userName = userName
        self.email = email
        self.password = password



# 定义一个可以访问自定义表单类的访问路径
def register():
    form = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate():
        user = User(form.userName.data, form.email.data, form.password.data)
        # db_session.add(user)

if __name__ == '__main__':
    print("wtforms测试！！！")

    print("打开数据库链接！")

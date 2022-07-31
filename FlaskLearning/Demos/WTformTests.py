# coding=gbk
'''
������WTform
1��TextField����ʾ<input type ='text'> HTML��Ԫ��
2��BooleanField����ʾ<input type ='checkbox'> HTML��Ԫ��
3��DecimalField��������ʾ��С�������ֵ��ı��ֶ�
4��IntegerField��������ʾ�������ı��ֶ�
5��RadioField����ʾ<input type = 'radio'> HTML��Ԫ��
6��SelectField����ʾѡ���Ԫ��
7��TextAreaField����ʾ<textarea> HTML��Ԫ��
8��PasswordField����ʾ<input type = 'password'> HTML��Ԫ��
9��SubmitField����ʾ<input type = 'submit'>��Ԫ��
'''

import pymysql
from flask import Flask, request
from wtforms import Form, BooleanField, StringField, PasswordField, validators

app = Flask(__name__)

# ע��һ����¼����
class RegistrationForm(Form):
    user = StringField('userName', [validators.Length(min=4, max=25)])
    email = StringField('email', [validators.Length(min=6, max=25)])
    password = PasswordField('password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='�������һ�£�')
    ])
    confirm = PasswordField('���ظ�����һ�����룡')
    accept_tos = BooleanField('���յ�¼��', [validators.DataRequired()])


# ����һ��User��
class User:
    def __init__(self, userName, email, password):
        self.userName = userName
        self.email = email
        self.password = password



# ����һ�����Է����Զ������ķ���·��
def register():
    form = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate():
        user = User(form.userName.data, form.email.data, form.password.data)
        # db_session.add(user)

if __name__ == '__main__':
    print("wtforms���ԣ�����")

    print("�����ݿ����ӣ�")

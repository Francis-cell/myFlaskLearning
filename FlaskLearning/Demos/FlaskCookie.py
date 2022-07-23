# coding=gbk
from flask import Flask, render_template, make_response, request

app = Flask(__name__)

@app.route("/set_cookies")
def set_cookie():
    resp = make_response('success')
    # ����cookie--zmrs��ֵΪzmrs1����Чʱ��Ϊ1h
    resp.set_cookie("zmrs", "zmrs1", max_age=3600)
    return resp

@app.route("/get_cookies")
def get_cookie():
    # ��ȡ����Ϊzmrs��Ӧcookie��ֵ
    cookie_temp = request.cookies.get("zmrs")
    return cookie_temp

@app.route("/delete_cookies")
def delete_cookie():
    resp = make_response("del success")
    resp.delete_cookie("zmrs")
    return resp

if __name__ == '__main__':
    print("Flask Cooike���ԣ�����")
    app.run(debug=True)
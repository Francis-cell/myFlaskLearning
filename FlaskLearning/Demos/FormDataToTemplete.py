# coding=gbk
from flask import Flask, render_template, request

app = Flask(__name__, template_folder="../templates", static_folder="../staticFiles")


@app.route("/")
def student():
    return render_template('FormDataToTemplete.html')


@app.route("/result", methods=['POST', 'GET'])
def result():
    if request.method == 'POST':
        result = request.form
        return render_template('FormDataToTemplete_result.html', result=result)

if __name__ == '__main__':
    print("���������ݵ�ģ��ʹ�ã�����")
    app.run(debug=True)
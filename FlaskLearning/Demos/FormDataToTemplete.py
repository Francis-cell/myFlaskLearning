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
        print(result)
        print(type(result))
        return render_template('FormDataToTemplete_result.html', result=result)
        # return render_template('FormDataToTemplete.html', result=result)


if __name__ == '__main__':
    print("表单发送数据到模板使用！！！")
    app.run(debug=True)
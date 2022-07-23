# coding=gbk

from flask import Flask, render_template

app = Flask(__name__, template_folder="../templates", static_folder="")

@app.route("/")
def index():
    # 向模板中传输数据
    my_str = "hello 123"
    my_int = 11
    my_array = [1, 2, 3, 4, 5]
    my_dict = {
        'name' : 'zmr',
        'age' : 23,
    }
    return render_template('dataFlush.html',
                           my_str = my_str,
                           my_array = my_array,
                           my_int = my_int,
                           my_dict = my_dict)


if __name__ == '__main__':
    print("数据渲染!!!")
    app.run()
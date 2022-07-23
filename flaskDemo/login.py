# coding=gbk

# 导入Flask模块
from flask import Flask
# 导入解析html页面的模块
from flask import render_template

# 新建一个Flask实例
'''
参数说明：
    1、__name__: 参数名称
    2、template_folder: 指定html页面所在的路径
    3、static_folder: 指定静态资源文件(图片,bootStrap等文件所在的路径)
'''
app = Flask(__name__, template_folder="../html", static_folder="")

@app.route('/')
def login():
    # 解析html模板
    return render_template('login.html')


if __name__ == '__main__':
    app.run()
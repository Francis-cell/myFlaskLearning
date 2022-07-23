# coding=gbk
import os
from flask import Flask, request, render_template
from werkzeug.utils import secure_filename

'''
## 1、基本使用
其 `enctype` 属性设置为“`multipart/form-data”`将文件发布到 URL
URL 处理程序从 `request.files[]`对象中提取文件，并将其保存到所需的位置。

## 2、文件名获取
目标文件的名称可以是硬编码的，也可以从 `request.files[file] `对象的` filename `属性中获取。
但是，建议使用 `secure_filename()` 函数获取它的安全版本。

## 3、默认上传文件夹的路径和上传文件的最大大小
app.config['UPLOAD_FOLDER'] 定义上传文件夹的路径 
app.config['MAX_CONTENT_LENGTH'] 指定要上传的文件的最大大小（以字节为单位）
'''

app = Flask(__name__, template_folder="../templates")
# 注意：app.config['UPLOAD_FOLDER'] = 'upload/'
# upload 前面不能加“/"
app.config['UPLOAD_FOLDER'] = '../upload/'

@app.route("/upload")
def upload_file():
    return render_template("uploadFiles.html")

'''
文件上传之后，执行保存的方法
'''
@app.route("/uploader", methods=["GET", "POST"])
def uploader():
    if request.method == 'POST':
        f = request.files["file"]
        # 执行保存操作(os.path.join() --- 方法说明：将路径不同部分拼接成一个完整的路径)
        # app.config['UPLOAD_FOLDER'] 定义上传文件夹的路径
        f.save(os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(f.filename)))
        return "文件保存成功！！！"
    else:
        return render_template("uploadFiles.html")


if __name__ == '__main__':
    print("文件上传测试！！！")
    app.run(debug=True)
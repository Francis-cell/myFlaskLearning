# coding=gbk
import os
from flask import Flask, request, render_template
from werkzeug.utils import secure_filename

'''
## 1������ʹ��
�� `enctype` ��������Ϊ��`multipart/form-data��`���ļ������� URL
URL �������� `request.files[]`��������ȡ�ļ��������䱣�浽�����λ�á�

## 2���ļ�����ȡ
Ŀ���ļ������ƿ�����Ӳ����ģ�Ҳ���Դ� `request.files[file] `�����` filename `�����л�ȡ��
���ǣ�����ʹ�� `secure_filename()` ������ȡ���İ�ȫ�汾��

## 3��Ĭ���ϴ��ļ��е�·�����ϴ��ļ�������С
app.config['UPLOAD_FOLDER'] �����ϴ��ļ��е�·�� 
app.config['MAX_CONTENT_LENGTH'] ָ��Ҫ�ϴ����ļ�������С�����ֽ�Ϊ��λ��
'''

app = Flask(__name__, template_folder="../templates")
# ע�⣺app.config['UPLOAD_FOLDER'] = 'upload/'
# upload ǰ�治�ܼӡ�/"
app.config['UPLOAD_FOLDER'] = '../upload/'

@app.route("/upload")
def upload_file():
    return render_template("uploadFiles.html")

'''
�ļ��ϴ�֮��ִ�б���ķ���
'''
@app.route("/uploader", methods=["GET", "POST"])
def uploader():
    if request.method == 'POST':
        f = request.files["file"]
        # ִ�б������(os.path.join() --- ����˵������·����ͬ����ƴ�ӳ�һ��������·��)
        # app.config['UPLOAD_FOLDER'] �����ϴ��ļ��е�·��
        f.save(os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(f.filename)))
        return "�ļ�����ɹ�������"
    else:
        return render_template("uploadFiles.html")


if __name__ == '__main__':
    print("�ļ��ϴ����ԣ�����")
    app.run(debug=True)
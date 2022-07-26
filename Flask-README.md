# Flask

## 0、参考链接

1、[教程](https://dormousehole.readthedocs.io/en/latest/tutorial/index.html)

2、[Python Flask框架：零基础web开发入门教程](https://segmentfault.com/a/1190000017330435)

3、[Flask学习主要参考文章](https://www.w3cschool.cn/flask) ==一期参考资料==



4、[Python的Flask框架中生成==SECRET_KEY==密钥](https://www.gaodaima.com/218641.html)





## 1、基本使用

### 1、app.run

```python
# 参数可选
# host： 要监听的主机名。 默认为127.0.0.1（localhost）。设置为“0.0.0.0”以使服务器在外部可用
# port： 默认值为5000
# debug： 默认为false。 如果设置为true，则提供调试信息
# options：要转发到底层的Werkzeug服务器。
app.run(host, port, debug, options)
```





### 2、HTTP方法

请求时使用的表单如下：(使用的请求方式为POST)

```html
<html>
   <body>
      <form action = "http://localhost:5000/login" method = "post">
         <p>Enter Name:</p>
         <p><input type = "text" name = "nm" /></p>
         <p><input type = "submit" value = "submit" /></p>
      </form>
   </body>
</html>
```

当表单请求方式为==POST方式==的时候

```python
# 获取"nm"的值的方式
user = request.form["nm"]
```

当表单请求方式为==GET方式==的时候

```python
# 获取"nm"的值的方式
user = request.args.get('nm')
```





### 3、request对象

​	  **request01.py**

```bash
"Form" - 它是一个字典对象，包含表单参数及其值的键和值对。
"args" - 解析查询字符串的内容，它是问号（？）之后的URL的一部分。
"Cookies"  - 保存Cookie名称和值的字典对象。
"files" - 与上传文件有关的数据。
"method" - 当前请求方法。
```





### 4、Cookies

​      **FlaskCookie.py**

#### 1、设置cookie

```python
# 设置cookie,默认有效期是临时cookie,浏览器关闭就失效
# 可以通过 max_age 设置有效期， 单位是秒
# 设置响应体
resp = make_response("success") 
# 这里的cookie的名字为zmr，cookie的值为zmrs
resp.set_cookie("zmr", "zmrs", max_age=3600)
```



#### 2、获取cookie

```python
# 通过request.cookies的方式， 返回的是一个字典，可以获取字典里的相应的值
# 获取指定名字的cookie对应的value的值
cookies = request.cookies.get("zmr")
```



#### 3、删除cookie

```python
# 这里的删除只是让cookie过期，并不是直接删除cookie
#  删除cookie，通过delete_cookie()的方式， 里面是cookie的名字
# 设置响应体
resp = make_response("del success")  
# 删除指定name的cookie的value值，但是这个cookie的name并不会被删掉
resp.delete_cookie("zmr")
```





### 5、会话

​	  **SessionTest.py**

```python
# 设置一个'username'会话变量
session['username'] = 'admin'

# 释放会话变量
session.pop('username', None)

'''
会话数据存储在cookie的顶部，服务器以加密方式对其进行签名
对于此加密，Flask应用程序需要一个定义的SECRET_KEY
'''
# 例如
app.secret_key = "xioieipcjmd3bfra2h"
```





### 6、重定向和错误

​	  **redirectAndError.py**

#### 1、重定向

```python
# 重定向
# location参数是应该重定向响应的URL。
# statuscode发送到浏览器标头，默认为302。
# response参数用于实例化响应。
Flask.redirect(location, statuscode, response)
```



#### 2、标准状态码

```bash
HTTP_300_MULTIPLE_CHOICES
HTTP_301_MOVED_PERMANENTLY
HTTP_302_FOUND
HTTP_303_SEE_OTHER
HTTP_304_NOT_MODIFIED
HTTP_305_USE_PROXY
HTTP_306_RESERVED
HTTP_307_TEMPORARY_REDIRECT
```



#### 3、错误

```python
Flask.abort(code)
```



#### 4、错误码

```bash
400 - 用于错误请求
401 - 用于未身份验证的
403 - Forbidden
404 - 未找到
406 - 表示不接受
415 - 用于不支持的媒体类型
429 - 请求过多
```







## 2、扩展

### 1、关于==`secret_key`==

```bash
# SECRET_KEY 配置变量是通用密钥, 可在 Flask 和多个第三方扩展中使用.

考虑到"安全性", 这个密钥是"不建议存储在你的程序中"的
最好的方法是存储在你的系统环境变量中, 通过&nbsp;os.getenv(key, default=None)&nbsp;获得
```






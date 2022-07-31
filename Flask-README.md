# Flask

## 0、参考链接

1、[教程](https://dormousehole.readthedocs.io/en/latest/tutorial/index.html)

2、[Python Flask框架：零基础web开发入门教程](https://segmentfault.com/a/1190000017330435)

3、[Flask学习主要参考文章](https://www.w3cschool.cn/flask) ==一期参考资料==



4、[Python的Flask框架中生成==SECRET_KEY==密钥](https://www.gaodaima.com/218641.html)



==问题类==

1、[记踩坑--Flask Web开发：S6电子邮件 ----[Errno 11004\] getaddrinfo failed](https://www.cnblogs.com/liangmingshen/p/10162153.html)





==扩展类==

1、[Python fields.TextField方法代码示例](https://vimsky.com/examples/detail/python-method-wtforms.fields.TextField.html)




## 1、基本使用

### 1、Flask Request 对象

```bash
Form - 它是一个字典对象，包含表单参数及其值的键和值对

args - 解析查询字符串的内容，它是问号（？）之后的URL的一部分

Cookies  - 保存Cookie名称和值的字典对象

files - 与上传文件有关的数据

method - 当前请求方法
```





## 2、扩展

### 1、关于==`secret_key`==

```bash
# SECRET_KEY 配置变量是通用密钥, 可在 Flask 和多个第三方扩展中使用.

考虑到"安全性", 这个密钥是"不建议存储在你的程序中"的
最好的方法是存储在你的系统环境变量中, 通过&nbsp;os.getenv(key, default=None)&nbsp;获得
```






# coding=gbk

'''
方法说明：输入需要的密码的长度，随机生成对应长度的密码
参数说明：password_length: 需要生成的密码的长度
返回值：生成的最终的密码
举例： password_length： 7
'''

def createPassword(password_length):
    import random
    password_last = ""
    s = "abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*"
    # s = "abcdefghijklmnopqrstuvwxyz0123456789"
    # 生成没有重复元素的随机密码
    # password_last = "".join(random.sample(s, password_length))

    # 生成可以有重复元素的随机密码
    for i in range(0, password_length):
        password_last += random.choice(s)
    return password_last


if __name__ == '__main__':
    password_length = int(input("请输入需要生成的密码位数:"))
    print(createPassword(password_length))

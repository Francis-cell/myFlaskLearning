# coding=gbk

'''
����˵����������Ҫ������ĳ��ȣ�������ɶ�Ӧ���ȵ�����
����˵����password_length: ��Ҫ���ɵ�����ĳ���
����ֵ�����ɵ����յ�����
������ password_length�� 7
'''

def createPassword(password_length):
    import random
    password_last = ""
    s = "abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*"
    # s = "abcdefghijklmnopqrstuvwxyz0123456789"
    # ����û���ظ�Ԫ�ص��������
    # password_last = "".join(random.sample(s, password_length))

    # ���ɿ������ظ�Ԫ�ص��������
    for i in range(0, password_length):
        password_last += random.choice(s)
    return password_last


if __name__ == '__main__':
    password_length = int(input("��������Ҫ���ɵ�����λ��:"))
    print(createPassword(password_length))

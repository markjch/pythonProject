#coding:utf-8
import time
def show_info():
    print('请输入提示数字，执行相应操作：0.退出1.查看登录日志')

def write_logininfo(username):
    with open('log.txt','a') as file:
        s=f'用户名{username},登陆时间：{time.strftime("%Y-%m_%d %H:%M:%S",time.localtime(time.time()))}'
        file.write(s)
        file.write('\n')

def read_logininfo():
    with open('log.txt','r') as file:
        while True:
            line=file.readline()
            if line=='':
                break
            else:
                print(line,end='')

if __name__ == '__main__':
    username=input('请输入用户名：')
    pwd=input('请输入密码：')
    if 'a'==username and 'a'==pwd:
        print('登陆成功！')
        write_logininfo(username)
        show_info()
        num=int(input('请输入操作数字：'))
        while True:
            if num==0:
                print('退出成功！')
                break
            elif num==1:
                print('查看登录日志')
                read_logininfo()
                num=int(input('请输入操作数字：'))
            else:
                print('您输入有误，请重新输入！')
                show_info()
                num=int(input('输入操作数字：'))
    else:
        print('用户名或密码不正确！')
    print(time.time())
    print(time.localtime())
    print(time.strftime("%Y-%m_%d %H:%M:%S",time.localtime(time.time())))
# p169
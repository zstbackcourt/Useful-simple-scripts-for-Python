# -*- coding:utf-8 -*-
"""
测试ssh是否连通的脚本(当知道部分ip,用户名和密码但不确定具体ip时,暴力测试)
@author: Weijie Shen
"""
import paramiko
class Server():
    def __init__(self, ip, username, password):
        self.username = username
        self.password = password
        self.ip = ip
        self.connect_result = ""

    # ssh登陆并反馈连接成功或失败信息
    def connect(self):
        # 实例化SSHClient
        conn = paramiko.SSHClient()
        # 自动添加策略，保存服务器的主机名和密钥信息，如果不添加，那么不再本地know_hosts文件中记录的主机将无法连接
        conn.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        try:
            # 尝试连接,如果成功则打印相应的ip,用户名和密码
            conn.connect(self.ip, username=self.username, password=self.password)
            self.connection = conn
            self.connect_result = "Connect Server {0} {1} {2} Successfully!\n".format(
                self.ip, self.username, self.password)
            return self.connect_result,True
        except:
            # 不成功则不打印
            self.connect_result = "Connect Server {0} {1} {2} Failed!\n".format(
                self.ip, self.username, self.password)
            return self.connect_result,False


if __name__ == '__main__':
    isFind = False # flag用于记录有没有找到服务器
    for i in range(0,256):
        ip = "172.16.0."+str(i)
        username = "amax"
        password = "szx19960422"
        conn = Server(ip, username, password)
        connection_result,isFind = conn.connect()
        if isFind:
            print(connection_result)
            break
        else:
            print(connection_result)



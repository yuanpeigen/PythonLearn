import socket
import sys

'''Socket客户端'''


class Client:
    def __init__(self, host):
        self.host = host  # 待连接的远程主机域名

    def connect(self):  # 连接方法
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        except socket.error as e:
            print('Failed to create socket,error:', e)
            sys.exit()  # 退出进程
        try:
            remote_ip = self.host  # 获取ip
        except socket.gaierror:
            print('主机无法被解析')
            sys.exit()  # 退出进程
        try:
            s.connect((remote_ip, 8800))  # 连接
            print('============连接服务端成功=============')
            while True:
                inp = input('>>>请发送指令：')
                if inp == 'exit':
                    print('已下线！')
                    s.close()  # 关闭连接
                    break
                message = bytes(inp, encoding='utf-8')
                s.sendall(message)  # 发送数据
                # 接收服务端数据
                try:
                    reply = s.recv(4096)  # 接收数据
                    print('收到服务端指令：' + str(reply, encoding='utf-8'))
                except socket.error:
                    print('============与服务端连接中断=============')
                    break
        except socket.error:
            print('============连接服务端失败============')
            sys.exit()  # 退出进程


if __name__ == '__main__':
    cl = Client('127.0.0.1')
    cl.connect()

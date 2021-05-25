import socket
import sys
import os
import re


class Client:
    def __init__(self, ip, port):
        self.serverIp = ip
        self.serverPort = port
        self.bufferSize = 10240

    def connect(self):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        except socket.error as e:
            print('Failed to create socket. Error:', e)

        try:
            s.connect((self.serverIp, self.serverPort))
            while True:
                message = input('> ')  # 接收用户输入
                if not message:
                    break
                s.send(bytes(message, 'utf-8'))  # 发送命令
                data = s.recv(self.bufferSize)  # 接收数据
                if not data:
                    break
                if re.search('^0001', data.decode('utf-8', 'ignore')):  # 判断数据类型
                    print(data.decode('utf-8')[4:])
                else:  # 文件内容处理
                    s.send('File size received'.encode())  # 通知服务端可以发送文件了
                    file_total_size = int(data.decode())  # 总大小
                    received_size = 0
                    f = open(f'new_{os.path.split(message)[-1]}', 'wb')  # 创建文件
                    while received_size < file_total_size:
                        data = s.recv(self.bufferSize)
                        f.write(data)  # 写文件
                        received_size += len(data)  # 累计接收长度
                        print('已接收：', received_size)
                    f.close()  # 关闭文件
                    print("receive done", file_total_size, " ", received_size)
        except socket.error:
            s.close()
            '''单独一个 raise，该语句引发当前上下文中捕获的异常（比如在 except 块中），或默认引发 RuntimeError 异常'''
            raise  # 退出进程
        finally:
            s.close()


if __name__ == '__main__':
    cl = Client('127.0.0.1', 8800)
    cl.connect()

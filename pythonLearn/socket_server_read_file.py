import socket
import sys
import os


class Server:
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        self.bufferSize = 10240

    def start(self):  # 启动监听，接收数据
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            s.bind((self.ip, self.port))  # 绑定
            s.listen(10)  # 监听
            print('等待客户端连接')
            while True:  # 一直等待新的连接
                try:
                    conn, addr = s.accept()  # 接收连接
                    print(f'客户端连接，{addr[0]}:{addr[1]}')
                    while True:  # 保持长连接
                        data = conn.recv(self.bufferSize)  # 接收数据
                        if not data:  # 断开连接时退出当前循环
                            break
                        else:
                            self.executeCommand(conn, data)
                    conn.close()  # 关闭当前连接
                except socket.error as e:
                    print(e)
        finally:
            s.close()  # 关闭服务端

    def executeCommand(self, conn, data):  # 解析并执行命令
        try:
            message = data.decode('utf-8')
            # 判断是否是文件
            if os.path.isfile(message):
                # 获取文件大小
                filesize = str(os.path.getsize(message))
                print('文件大小为:', filesize)
                # 发送文件大小
                conn.send(filesize.encode())
                data = conn.recv(self.bufferSize)
                print('开始发送')
                # 打开文件
                f = open(message, 'rb')
                for line in f:
                    # 发送文件内容
                    conn.send(line)
                print('发送完成')
            else:
                print('收到指令：', message)
                conn.send(('0001' + os.popen(message).read()).encode('utf-8'))
        except:
            raise


if __name__ == '__main__':
    s = Server('', 8800)
    s.start()

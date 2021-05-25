import socket
import sys

'''Socket服务端'''


class Server:
    def __init__(self, ip, port):
        self.port = port
        self.ip = ip

    def start(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 创建socket
        try:
            s.bind((self.ip, self.port))  # 绑定
            s.listen(10)  # 监听,支持同时挂起10个连接
            print('+++++++++++++等待客户端连接+++++++++++++')
            while True:
                conn, addr = s.accept()  # 接收连接
                print('+++++++++++++' + str(addr) + '上线+++++++++++++')
                while True:
                    try:
                        data = conn.recv(1024)  # 接收数据
                        if not data:
                            conn.close()  # 关闭连接
                            break
                        print(f'客户端指令：{str(data, encoding="utf-8")}')
                        inp = input('>>>请输入指令：')
                        conn.sendall(bytes(inp, encoding='utf-8'))  # 发送数据
                    except ConnectionResetError:
                        print('+++++++++++++客户端离线+++++++++++++')
                        break
        except socket.error as e:
            print(e)
            sys.exit()
        finally:
            s.close()  # 关闭服务端


if __name__ == '__main__':
    s = Server('', 8800)
    s.start()

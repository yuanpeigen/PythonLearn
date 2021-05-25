import socket
import sys
import selectors
import types


class Server:
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        self.selector = selectors.DefaultSelector()  # 初始化selector

    def start(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            s.bind((self.ip, self.port))
            s.listen()
            print('等待监听：', (self.ip, self.port))
            s.setblocking(False)  # 非阻塞
            self.selector.register(s, selectors.EVENT_READ, None)  # 注册I/O对象
            while True:
                events = self.selector.select(timeout=None)  # 阻塞调用，等待新的读写事件
                for key, mask in events:
                    if key.data is None:  # 收到新的连接请求
                        self.accept_wrapper(key.fileobj)
                    else:  # 收到客户端连接发送的数据
                        self.service_connection(key, mask)
        except socket.error as e:
            print(e)
            sys.exit()
        finally:
            s.close()  # 关闭服务端

    def accept_wrapper(self, sock):
        conn, addr = sock.accept()
        print('接收客户端连接', addr)
        conn.setblocking(False)  # 非阻塞
        data = types.SimpleNamespace(addr=addr, inb=b'', outb=b'')  # socket数据
        events = selectors.EVENT_READ | selectors.EVENT_WRITE  # 监听读写
        self.selector.register(conn, events, data=data)  # 注册客户端socket

    def service_connection(self, key, mask):
        sock = key.fileobj
        data = key.data
        if mask & selectors.EVENT_READ:
            recv_data = sock.recv(1024)  # 接收数据
            if recv_data:
                data.outb += recv_data
            else:  # 客户端断开连接
                print('连接断开：', data.addr)
                self.selector.unregister(sock)  # 取消注册，防止出错
                sock.close()
        if mask & selectors.EVENT_WRITE:
            if data.outb:
                print('echoing', repr(data.outb), 'to', data.addr)
                send = sock.send(data.outb)
                data.outb = data.outb[send:]  # 缓存数据


if __name__ == '__main__':
    s = Server('', 8800)
    s.start()

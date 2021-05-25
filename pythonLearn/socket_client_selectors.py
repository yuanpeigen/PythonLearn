import socket
import sys
import selectors
import types


class Client:
    def __init__(self, host, port, num_conn=5):
        self.host = host
        self.port = port
        self.num_conn = num_conn
        self.selector = selectors.DefaultSelector()
        self.message = [b'message 1 from client', b'message 1 from client']

    def connect(self):
        server_addr = (self.host, self.port)
        for i in range(self.num_conn):
            conn_id = i + 1
            print('开始连接', conn_id, '到', server_addr)
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.setblocking(False)  # 非阻塞
            sock.connect_ex(server_addr)  # 连接服务端
            events = selectors.EVENT_WRITE | selectors.EVENT_READ
            data = types.SimpleNamespace(connid=conn_id, msg_total=sum(len(m) for m in self.message), recv_total=0,
                                         messages=list(self.message), outb=b'')
            self.selector.register(sock, events, data=data)
        try:
            while True:
                events = self.selector.select(timeout=1)
                if events:
                    for key, mask in events:
                        self.service_connection(key, mask)
                else:
                    break
        finally:
            self.selector.close()

    def service_connection(self, key, mask):
        sock = key.fileobj
        data = key.data
        if mask & selectors.EVENT_READ:
            recv_data = sock.recv(1024)
            if recv_data:
                print('收到', repr(recv_data), '来自连接：', data.connid)
                data.recv_total += len(recv_data)

            if not recv_data or data.recv_total == data.msg_total:  # 根据接收数据的长度，判断是否关闭客户端
                print('关闭连接,', data.connid)
                self.selector.unregister(sock)
                sock.close()
        if mask & selectors.EVENT_WRITE:
            if not data.outb and data.messages:
                data.outb = data.messages.pop(0)
            if data.outb:
                print('发送', repr(data.outb), '到连接', data.connid)
                send = sock.send(data.outb)  # 发送数据
                data.outb = data.outb[send:]  # 清空数据


if __name__ == '__main__':
    cl = Client('127.0.0.1', 8800)
    cl.connect()

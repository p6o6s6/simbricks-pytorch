import socket

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('10.0.0.1', 13345))
    server_socket.listen(5)
    print('服务器启动，监听端口：13345...')

    while True:
        conn, addr = server_socket.accept()
        print('收到来自:', addr, '的连接请求.')

        data = conn.recv(1024)
        if not data:
            break
        print('收到:', data.decode('utf-8'))
        conn.send(data.upper())

        conn.close()
        print('与', addr, '的连接已关闭.')
        break  # 只处理一次连接请求，然后就断开连接

if __name__ == '__main__':
    start_server()
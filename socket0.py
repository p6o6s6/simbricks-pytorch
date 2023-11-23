import socket
import threading

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('10.0.0.1', 13345))  # 更改为本地host
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

def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('10.0.0.1', 13345))
    print('成功连接到服务器')

    data = "123"
    client_socket.send(data.encode('utf-8'))
    print('已发送消息: ', data)

    recv_data = client_socket.recv(1024)
    print('收到:', recv_data.decode('utf-8'))

    client_socket.close()
    print('与服务器的连接已关闭.')

if __name__ == '__main__':
    # 创建并启动服务器线程
    server_thread = threading.Thread(target=start_server)
    server_thread.start()

    # 等待服务器启动
    import time
    time.sleep(1)

    # 创建并启动客户端线程
    client_thread = threading.Thread(target=start_client)
    client_thread.start()
import socket

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
    start_client()
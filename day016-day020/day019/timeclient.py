from socket import socket, AF_INET, SOCK_STREAM


def main():
    # 1、创建套接字 socket
    client_socket = socket(family=AF_INET, type=SOCK_STREAM)
    # 2、连接服务器
    client_socket.connect(('10.7.152.89', 9999))

    # 3、循环发送和接收信息
    while True:
        info = client_socket.recv(1024).decode('utf-8')
        print(info)
        # client_socket.close()


if __name__ == '__main__':
    main()

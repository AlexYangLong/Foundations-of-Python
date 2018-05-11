from socket import socket


def main():
    client = socket()
    client.connect(('10.7.152.89', 9999))
    print('连接服务器成功......')

    while True:
        client_info = input('>>>')
        client.send(client_info.encode('utf-8'))

        server_info = client.recv(1024).decode('utf-8')
        # if server_info:
        print('服务器回复到：' + server_info)

        if client_info == 'bye' or server_info == 'bye':
            break


if __name__ == '__main__':
    main()
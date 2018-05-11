from socket import socket


def main():
    server = socket()
    server.bind(('10.7.152.89', 9999))
    server.listen(512)
    print('服务器启动成功......')

    while True:
        client, addr = server.accept()
        print(str(addr) + '连接到服务器')

        while True:
            client_info = client.recv(1024).decode('utf-8')
            # if client_info:
            print(str(addr) + '说：' + client_info)

            server_info = input('>>>')
            client.send(server_info.encode('utf-8'))

            if server_info == 'bye' or client_info == 'bye':
                break
        client.close()


if __name__ == '__main__':
    main()

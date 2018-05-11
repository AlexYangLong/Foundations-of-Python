from socket import socket


def main():
    server = socket()
    server.bind(('10.7.152.89', 9999))
    server.listen(512)
    while True:
        client, addr = server.accept()
        print(str(addr) + '连接到服务器')

        while True:
            info = client.recv(1024).decode('utf-8')
            print(str(addr) + '说：' + info)
            client.send(info.encode('utf-8'))
            if info == 'bye':
                break
        client.close()


if __name__ == '__main__':
    main()

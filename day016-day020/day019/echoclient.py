from socket import socket


def main():
    client = socket()
    client.connect(('10.7.152.89', 9999))

    while True:
        info = input('对服务器说：')
        client.send(info.encode('utf-8'))

        res = client.recv(1024).decode('utf-8')
        print(res)
        if info == 'bye':
            break


if __name__ == '__main__':
    main()
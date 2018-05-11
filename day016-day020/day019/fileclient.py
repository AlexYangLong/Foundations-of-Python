from socket import socket


def main():
    client = socket()
    client.connect(('10.7.152.89', 9999))
    print('连接服务器成功......')

    filename = client.recv(1024).decode('utf-8')
    print(filename)
    file_len = int(client.recv(1024).decode('utf-8'))
    print(file_len)

    with open(filename, 'wb') as fw:
        total = 0
        while total < file_len:
            fw.write(client.recv(1024))
            total += 1024
    print('图片接收成功')


if __name__ == '__main__':
    main()

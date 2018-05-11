from io import SEEK_END
from socket import socket
from time import sleep


def main():
    server = socket()
    server.bind(('10.7.152.89', 9999))
    server.listen(512)
    print('服务器启动成功......')

    with open('./1.jpg', 'rb') as fr:
        content = fr.read()
        # print(content)
        fr.seek(0, SEEK_END)  #  将文件指针移至文件末尾
        file_len = fr.tell()  #  fr.tell()  可以获取文件的大小

    while True:
        client, addr = server.accept()
        print(str(addr) + '连接到服务器')

        client.send('bak1.jpg'.encode('utf-8'))
        sleep(0.001)
        client.send(str(file_len).encode('utf-8'))
        sleep(0.001)
        total = 0
        while total < file_len:
            client.send(content[total:total + 1024])
            total += 1024
            sleep(0.001)

        client.close()
        print('图片发送完毕')


if __name__ == '__main__':
    main()

import json
from socket import socket, SOCK_STREAM, AF_INET
from base64 import b64decode


def main():
    client = socket(family=AF_INET, type=SOCK_STREAM)
    client.connect(('10.7.152.89', 9999))
    print('服务器连接成功......')

    # 用于保存接收服务器传过来的二进制数据
    data_bytes = bytes()
    data = client.recv(1024)
    while data:
        data_bytes += data
        data = client.recv(1024)

    dict_data = json.loads(data_bytes.decode('utf-8'))  # 将json转成字典
    filename = dict_data['filename']
    filedata = dict_data['filedata']
    with open(filename, 'wb') as fw:
        fw.write(b64decode(filedata.encode('utf-8')))  # 因为服务器对图片内容进行了解码，所以这里要进行编码

    print('图片接收成功')


if __name__ == '__main__':
    main()

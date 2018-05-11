from socket import socket, AF_INET, SOCK_STREAM
from base64 import b64encode
import json


def main():
    server = socket(family=AF_INET, type=SOCK_STREAM)
    server.bind(('10.7.152.89', 9999))
    server.listen(512)
    print('服务器启动成功......')

    with open('./1.jpg', 'rb') as fr:
        # 将读出的二进制数据进行base64编码, 得到的还是二进制数据，需要将二进制内容转成文本，要进行解码decode，注意：在客户端需要对内容进行编码encode
        content = b64encode(fr.read()).decode('utf-8')

    while True:
        client, addr = server.accept()
        print(str(addr) + '连接到服务器.')

        data_dict = {}
        data_dict['filename'] = '1-bak.jpg'
        data_dict['filedata'] = content
        data_json = json.dumps(data_dict)  # 将字典转成json

        client.send(data_json.encode('utf-8'))
        print('图片发送成功')

        client.close()


if __name__ == '__main__':
    main()

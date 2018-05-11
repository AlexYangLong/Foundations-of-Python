from socket import socket, AF_INET, SOCK_STREAM, SOCK_DGRAM
from datetime import datetime


def main():
    # 1、创建套接字对象，并指定使用哪种传输服务
    # AF_INET：IPV4 AF_INET6：IPV6  SOCK_STREAM: TCP  SOCK_DGRAM: UDP  SOCK_RAW: 原始套接字
    server_socket = socket(family=AF_INET, type=SOCK_STREAM)
    # 2、绑定IP地址和端口，建议使用 1024 以后的端口
    print('正在绑定IP地址和端口......')
    server_socket.bind(('10.7.152.89', 9999))
    print('服务器绑定IP地址和端口成功')
    # 3、启动监听 监听客户端有没有连接到服务器  512：历史经验最佳值
    print('正在启动服务器......')
    server_socket.listen(512)
    print('服务器启动成功')

    # 4、等待连接 通过循环等待客户端连接并作出相应处理
    while True:
        # 阻塞并等待连接
        client_socket, addr = server_socket.accept()
        print(str(addr) + '连接到了服务器.')

        # 5、发送数据
        client_socket.send(str(datetime.now()).encode('utf-8'))
        # 6、断开连接
        client_socket.close()


if __name__ == '__main__':
    main()

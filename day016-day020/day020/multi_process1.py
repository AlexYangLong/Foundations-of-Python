import random
from time import sleep, time
from multiprocessing import Process


def download(filename):
    print('开始下载——' + filename)
    delay = random.randint(5, 15)
    print('预计需要花费%d秒' % delay)
    sleep(random.randint(5, 15))
    print(filename + '下载完成')


def main():
    start = time()

    p1 = Process(target=download, args=('qqq',))
    p1.start()
    p2 = Process(target=download, args=('www',))
    p2.start()
    p3 = Process(target=download, args=('eee',))
    p3.start()

    # 等待三个进程执行完，再往后执行
    p1.join()
    p2.join()
    p3.join()
    end = time()

    print('总共花费%f秒' % (end - start))

if __name__ == '__main__':
    main()

import random
from time import sleep, time
from threading import Thread


def download(filename):
    print('开始下载——' + filename)
    delay = random.randint(5, 15)
    print('预计需要花费%d秒' % delay)
    sleep(random.randint(5, 15))
    print(filename + '下载完成')


def main():
    start = time()

    t1 = Thread(target=download, args=('qqq',))
    t1.start()
    t2 = Thread(target=download, args=('www',))
    t2.start()
    t3 = Thread(target=download, args=('eee',))
    t3.start()

    # 等待三个线程执行完，再往后执行
    t1.join()
    t2.join()
    t3.join()
    end = time()

    print('总共花费%f秒' % (end - start))

if __name__ == '__main__':
    main()

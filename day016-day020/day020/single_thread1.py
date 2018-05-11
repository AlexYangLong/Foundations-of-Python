import random
from time import sleep, time


def download(filename):
    print('开始下载——' + filename)
    delay = random.randint(5, 15)
    print('预计需要花费%d秒' % delay)
    sleep(random.randint(5, 15))
    print(filename + '下载完成')


def main():
    start = time()
    download('qqq')
    download('www')
    download('eee')
    end = time()

    print('总共花费%f秒' % (end - start))


if __name__ == '__main__':
    main()

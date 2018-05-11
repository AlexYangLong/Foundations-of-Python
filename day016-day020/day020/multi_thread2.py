import random
from time import sleep, time
from threading import Thread


def print_word(word):
    while True:
        print(word)
        sleep(1)


def main():
    t1 = Thread(target=print_word, args=('ping', ))
    t1.start()
    t2 = Thread(target=print_word, args=('pong', ))
    t2.start()

    # 等待线程执行完，再往后执行
    t1.join()
    t2.join()


if __name__ == '__main__':
    main()

from time import sleep

from os import system


class CountDown(object):
    def __init__(self, hour=0, minute=0, second=0):
        """
        初始化

        :param hour:
        :param minute:
        :param second:
        """
        self._hour = hour
        self._minute = minute
        self._second = second

    def show(self):
        """
        显示时间

        :return: 返回当前时间的字符串
        """
        return '%02d:%02d:%02d' % (self._hour, self._minute, self._second)

    def run(self):
        """走字"""
        self._second -= 1
        if self._second == -1:
            self._second = 59
            self._minute -= 1
            if self._minute == -1:
                self._minute = 59
                self._hour -= 1
                if self._hour == -1:
                    return False
        return True


def main():
    cd = CountDown(0, 1, 0)
    go_on = True
    while go_on:
        system('cls')
        print(cd.show())
        sleep(1)
        go_on = cd.run()
    print('倒计时结束')


if __name__ == '__main__':
    main()
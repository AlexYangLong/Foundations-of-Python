# 高内聚，低耦合
# 面向对象7原则、GoF设计模式(23中场景)
from time import sleep
from datetime import datetime
from os import system


class Clock(object):
    """数字时钟"""

    def __init__(self, hour=0, minute=0,second=0):
        """
        初始化方法

        :param hour: 时
        :param minute: 分
        :param second: 秒
        """
        self._hour = hour
        self._minute = minute
        self._second = second

    @classmethod
    def nowTime(cls):
        """
        获取当前时间，传入构造器

        :return:
        """
        now = datetime.now()
        return cls(now.hour, now.minute, now.second)

    def show(self):
        """
        显示时间

        :return: 返回当前时间的字符串
        """
        return '%02d:%02d:%02d' % (self._hour, self._minute, self._second)

    def run(self):
        """走字"""
        self._second += 1
        if self._second == 60:
            self._second = 0
            self._minute += 1
            if self._minute == 60:
                self._minute = 0
                self._hour += 1
                if self._hour == 24:
                    self._hour = 0


def main():
    # myClock = Clock(23, 59, 55)
    myClock = Clock.nowTime()
    while True:
        system('cls')  # system('cls') Windows 清屏， system('clear') Mac OS 清屏
        myClock.run()
        print(myClock.show())
        sleep(1)


if __name__ == '__main__':
    main()
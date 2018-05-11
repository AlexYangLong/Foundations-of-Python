from abc import abstractmethod


class Creature(object):
    pass


class Sallow(Creature):
    @abstractmethod
    def think(self):
        pass

    @abstractmethod
    def wander(self):
        pass


class Tree(Creature):
    @abstractmethod
    def less(self):
        pass


class Mine(Sallow, Tree):
    def think(self):
        return '随意找棵树休息翅膀'

    def wander(self):
        return '淡然飞向远方'

    def less(self):
        return '当枝头燕子飞去时\n再不用留恋张望\n'


def main():
    mine = Mine()

    if isinstance(mine, Sallow):
        print(mine.think())
        print(mine.wander())
    else:
        print('飞不过感情的墙')

    if isinstance(mine, Tree):
        print(mine.less())
    else:
        print('撑不破伤心的网')


if __name__ == '__main__':
    main()

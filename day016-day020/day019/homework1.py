
class Creature(object):
    pass


class Sallow(Creature):
    def think(self):
        return '只需简单思想'

    def wander(self):
        return '只求风中流浪'


class Tree(Creature):
    def less(self):
        return '不长六腑五脏\n不会寸断肝肠\n'


class Mine(Creature):
    pass


def main():
    mine = Mine()

    if isinstance(mine, Sallow):
        pass
    else:
        print('飞不过感情的墙')

    if isinstance(mine, Tree):
        pass
    else:
        print('撑不破伤心的网')


if __name__ == '__main__':
    main()

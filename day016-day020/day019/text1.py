from math import pi


class Circle(object):
    def __init__(self, radius):
        self.radius = radius

    def length(self):
        return 2 * pi * self.radius

    def square(self):
        return pi * self.radius * self.radius


def main():
    yyc_r = float(input('请输入游泳池半径：'))
    yyc = Circle(yyc_r)
    pd = Circle(yyc_r + 3)

    pd_s = 35.2 * (pd.square() - yyc.square())
    print('跑道地板造价：%.2f' % pd_s)

    pd_wq = 23.5 * pd.length()
    print('跑道围墙造价：%.2f' % pd_wq)


if __name__ == '__main__':
    main()

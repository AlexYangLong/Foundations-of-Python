from random import randint


class Computer(object):
    def __init__(self):
        self.number = randint(1, 100)
        self.res = ''
        self.counter = 0

    def compare(self, n):
        self.counter += 1
        if n > self.number:
            self.res = '小一点儿~'
        elif n < self.number:
            self.res = '大一点儿~'
        else:
            self.res = '恭喜你，猜对了.'
            if self.counter > 7:
                self.res += '但是，智商捉急~~~~'
            return True
        return False


def main():
    compuer = Computer()
    is_correct = False
    while not is_correct:
        yours = int(input('请输入：'))
        is_correct = compuer.compare(yours)
        print(compuer.res)


if __name__ == '__main__':
    main()

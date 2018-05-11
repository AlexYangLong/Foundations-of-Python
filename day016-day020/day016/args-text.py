

# *args  可变参数
# **kwargs  关键字参数
def add(*args, **kwargs):
    print(type(args))
    print(args)
    print(type(kwargs))
    print(kwargs)

    total = 0
    for val in args:
        total += val
    return total


# * 不是一个参数，只是一个分割符 后面表示 命名关键字参数
def sub(x, y, *, z):
    print(x, y, z)


# 在 *args 可变参数后面的，都是命名关键字参数
def fun(*args, x, y):
    print(args)
    print(x, y)


def main():
    # print(add())
    # print(add(1))
    # print(add(1, 2))
    # print(add(1, 3, 4, 5))
    # # *[] *()  表示将list、tuple中的元素拆分出来，变成单个元素
    # print(add(*[1,2,3,4,5]))
    # print(add(*(1,2,3,4,5)))

    print(add(20, 10, name='Alex', age=22))

    sub(12, 23, z=34)

    fun(34, 45, x=6, y=90)


if __name__ == '__main__':
    main()

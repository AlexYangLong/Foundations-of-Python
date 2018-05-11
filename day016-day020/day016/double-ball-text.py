from random import choice, sample


def ball_list():
    res_list = []
    red_ball_list = list(range(1, 34))
    blue_ball_list = list(range(1, 17))

    # sample(list, n)取样函数 从list中随机取 n 个 不会重复取
    # list1 = sample(red_ball_list, 6)
    # print(list1)

    for i in range(6):
        ball = choice(red_ball_list)
        red_ball_list.remove(ball)
        res_list.append(ball)
    # 给 list 排序
    # res_list = sorted(res_list)
    res_list.sort()
    # print(res_list)
    res_list.append(choice(blue_ball_list))
    return res_list


def main(num):
    for n in range(num):
        res_list = ball_list()
        for i in res_list:
            print('%02d' % i, end=' ')
        print()


if __name__ == '__main__':
    num = int(input('请输入你买的注数：'))
    main(num)

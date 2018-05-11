from random import randint


def roll_graps(num=2):
    total_sum = 0
    for i in range(num):
        total_sum += randint(1, 6)
    return total_sum


def main():
    first_sum = roll_graps(2)
    print('玩家摇出了%d 点' % first_sum)
    go_on = False

    if first_sum == 7 or first_sum == 12:
        print('玩家胜')
    elif first_sum == 2 or first_sum == 3 or first_sum == 12:
        print('庄家胜')
    else:
        go_on = True

    while go_on:
        after_sum = roll_graps(2)
        print('玩家摇出了%d 点' % after_sum)

        if after_sum == 7:
            print('庄家胜')
            go_on = False
        elif first_sum == after_sum:
            print('玩家胜')
            go_on = False


if __name__ == '__main__':
    main()
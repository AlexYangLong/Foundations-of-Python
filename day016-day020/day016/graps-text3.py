from random import randint


def roll_graps(num=2):
    total_sum = 0
    for i in range(num):
        total_sum += randint(1, 6)
    return total_sum


def main():
    computer_bet = 1000
    player_bet = 1000

    while computer_bet > 0 and player_bet > 0:
        player_stake = int(input('请输入赌注：'))
        first_sum = roll_graps(2)
        print('玩家摇出了%d 点' % first_sum)
        go_on = False

        if first_sum == 7 or first_sum == 12:
            player_bet += player_stake
            computer_bet -= player_stake
            print('玩家胜')
        elif first_sum == 2 or first_sum == 3 or first_sum == 12:
            player_bet -= player_stake
            computer_bet += player_stake
            print('庄家胜')
        else:
            go_on = True

        while go_on:
            after_sum = roll_graps(2)
            print('玩家摇出了%d 点' % after_sum)

            if after_sum == 7:
                player_bet -= player_stake
                computer_bet += player_stake
                print('庄家胜')
                go_on = False
            elif first_sum == after_sum:
                player_bet += player_stake
                computer_bet -= player_stake
                print('玩家胜')
                go_on = False

        print('电脑还有 %d ，玩家还有 %d' % (computer_bet, player_bet))


if __name__ == '__main__':
    main()
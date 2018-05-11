import random

def main():
    num_list = [1, 2, 3, 4, 5, 6]

    computer_bet = 100
    player_bet = 100

    flag = True

    while True:
        # computer_stake = int(input('请电脑输入赌注：'))
        # 这里还需要判断一下
        player_stake = int(input('请玩家输入赌注：'))
        computer_stake = player_stake

        graps1 = random.choice(num_list)
        graps2 = random.choice(num_list)

        print('骰子点数：%d  %d' % (graps1, graps2))

        if flag:
            first_sum = graps1 + graps2
        else:
            after_sum = graps1 + graps2

        if flag:
            if first_sum == 7 or first_sum == 12:
                player_bet += computer_stake
                computer_bet -= computer_stake
                print('玩家胜')
                # break
            elif first_sum == 2 or first_sum == 3 or first_sum == 12:
                player_bet -= computer_stake
                computer_bet += computer_stake
                print('庄家胜')
                # break
            else:
                flag = False
        else:
            if first_sum == after_sum:
                player_bet += computer_stake
                computer_bet -= computer_stake
                print('玩家胜')
                flag = True
                # break
            elif after_sum == 7:
                player_bet -= computer_stake
                computer_bet += computer_stake
                print('庄家胜')
                flag = True
                # break

        print('电脑赌资：%d, 玩家赌资：%d' % (computer_bet, player_bet))

        if computer_bet <= 0:
            print('电脑赌资输完了,游戏结束')
            break
        if player_bet <= 0:
            print('玩家赌资输完了,游戏结束')
            break


if __name__ == '__main__':
    main()
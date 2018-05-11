from random import shuffle

# 牌 face、type
class Card(object):
    def __init__(self, face, type):
        self.__face = face
        self.__type = type

    @property
    def face(self):
        return self.__face

    @property
    def type(self):
        return self.__type

    def __str__(self):
        return str(self.__face) + self.type

# 麻将 108张牌
class MahJang(object):
    def __init__(self):
        self.__mjList = []
        mjType = ['筒', '条', '万']
        for type in mjType:
            for i in range(4):
                for value in range(1, 10):
                    card = Card(value, type)
                    self.__mjList.append(card)

    @property
    def mjList(self):
        return self.__mjList

    # 洗牌
    def ShuffleCard(self):
        shuffle(self.__mjList)

class Player(object):
    def __init__(self, name):
        self.__name = name
        self.__cardList = []

    @property
    def name(self):
        return self.__name

    @property
    def cardList(self):
        return self.__cardList

    # 摸牌
    def touchCard(self, mjList, num):
        for i in range(num):
            card = mjList.pop(0)
            self.__cardList.append(card)

    # 整理牌面 按照 筒 条 万 从小到大排列
    def cleanupCard(self):
        tong_list = []
        tiao_list = []
        wan_list = []
        # 先分类
        for card in self.__cardList:
            if card.type == '筒':
                tong_list.append(card)
            elif card.type == '条':
                tiao_list.append(card)
            elif card.type == '万':
                wan_list.append(card)

        # 再排大小
        for j in range(len(tong_list)-1):
            for i in range((len(tong_list)-j-1)):
                if tong_list[i].face > tong_list[i+1].face:
                    # print(tong_list[i].face, tong_list[i+1].face)
                    temp = tong_list[i+1]
                    tong_list[i+1] = tong_list[i]
                    tong_list[i] = temp
        # for card in tong_list:
        #     print(card, end=',')
        # print()

        for j in range(len(tiao_list)-1):
            for i in range(len(tiao_list)-j-1):
                if tiao_list[i].face > tiao_list[i+1].face:
                    temp = tiao_list[i+1]
                    tiao_list[i+1] = tiao_list[i]
                    tiao_list[i] = temp

        for j in range(len(wan_list)-1):
            for i in range(len(wan_list)-j-1):
                if wan_list[i].face > wan_list[i+1].face:
                    temp = wan_list[i+1]
                    wan_list[i+1] = wan_list[i]
                    wan_list[i] = temp

        # tong_list = sorted(tong_list)
        # tiao_list = sorted(tiao_list)
        # wan_list = sorted(wan_list)

        self.__cardList = tong_list + tiao_list + wan_list

    def showCardList(self):
        for card in self.__cardList:
            print(card, end=',')
        print()

# 创建麻将列表
mahjang = MahJang()
print(len(mahjang.mjList))
mahjang.ShuffleCard()
for card in mahjang.mjList:
    print(card, end=',')
print()

# 创建玩家
player1 = Player('庄家')
player2 = Player('闲家1')
player3 = Player('闲家2')
player4 = Player('闲家3')

# 玩家摸牌
for i in range(3):
    player1.touchCard(mahjang.mjList, 4)
    player2.touchCard(mahjang.mjList, 4)
    player3.touchCard(mahjang.mjList, 4)
    player4.touchCard(mahjang.mjList, 4)

player1.touchCard(mahjang.mjList, 2)
player2.touchCard(mahjang.mjList, 1)
player3.touchCard(mahjang.mjList, 1)
player4.touchCard(mahjang.mjList, 1)

print(len(mahjang.mjList))

# 玩家整理牌面
player1.cleanupCard()
player2.cleanupCard()
player3.cleanupCard()
player4.cleanupCard()

# 展示
player1.showCardList()
player2.showCardList()
player3.showCardList()
player4.showCardList()


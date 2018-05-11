class Play(object):
    def __init__(self, num):
        self.num = num

    def compare(self, otherPlayer):
        if self.num > otherPlayer.num:
            return True
        else:
            return False


computer = Play(100)

player = Play(99)

print(player.compare(computer))


print('rd '.replace(' ', '%20'))
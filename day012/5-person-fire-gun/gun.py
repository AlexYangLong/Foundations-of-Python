class Gun(object):
    def __init__(self, bulletBox):
        self.bulletBox = bulletBox

    def shoot(self):
        if self.bulletBox.bulletCount == 0:
            print('已经没有子弹了，请装弹...')
        else:
            self.bulletBox.bulletCount -= 1
            if self.bulletBox.bulletCount == 0:
                print('最后一颗子弹已打完，请装弹...')
            else:
                print('还剩%d颗子弹' % self.bulletBox.bulletCount)
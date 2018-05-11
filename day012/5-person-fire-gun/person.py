class Person(object):
    def __init__(self, gun):
        self.gun = gun

    def fire(self):
        self.gun.shoot()

    def reload(self, count):
        if count == 0:
            print('你是在逗我吗？...')
        else:
            self.gun.bulletBox.bulletCount += count
            print('装弹成功！...')
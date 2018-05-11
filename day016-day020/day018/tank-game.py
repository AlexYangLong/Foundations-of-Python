from enum import Enum, unique
from time import sleep

import pygame

bg_color = (242, 242, 242)
green_color = (0, 255, 0)
red_color = (255, 0, 0)
blue_color = (0, 0, 255)
black_color = (0, 0, 0)


@unique
class Direct(Enum):
    """
    枚举是定义符号常量的最佳选择，符号常量优于字面常量
    @unique表示枚举类中的值每一个都是唯一的
    """
    UP = 1
    RIGHT = 2
    DOWN = 3
    LEFT = 4


class Bullet(object):
    def __init__(self, x, y, speed=10, direct=Direct.UP):
        self.x = x
        self.y = y
        self.speed = speed
        self.direct = direct

    def fly(self):
        if self.direct == Direct.UP:
            if self.y - self.speed >= 0:
                self.y -= self.speed
            else:
                self.y = 0
        elif self.direct == Direct.RIGHT:
            if self.x + self.speed < 800:
                self.x += self.speed
            else:
                self.x = 800
        elif self.direct == Direct.DOWN:
            if self.y + self.speed < 600:
                self.y += self.speed
            else:
                self.y = 600
        elif self.direct == Direct.LEFT:
            if self.x - self.speed > 0:
                self.x -= self.speed
            else:
                self.x = 0

    def draw(self, screen):
        pygame.draw.circle(screen, black_color, (self.x, self.y), 2, 0)


class Tank(object):
    def __init__(self, x, y, color=green_color, speed=5, direct=Direct.UP):
        self.x = x
        self.y = y
        self.color = color
        self.speed = speed
        self.direct = direct

    def move(self):
        if self.direct == Direct.UP:
            if self.y - 10 - self.speed > 0:
                self.y -= self.speed
            else:
                self.y = 10
        elif self.direct == Direct.RIGHT:
            if self.x + 39 + self.speed < 800:
                self.x += self.speed
            else:
                self.x = 800 - 39
        elif self.direct == Direct.DOWN:
            if self.y + 39 + self.speed < 600:
                self.y += self.speed
            else:
                self.y = 600 - 39
        elif self.direct == Direct.LEFT:
            if self.x - 10 - self.speed > 0:
                self.x -= self.speed
            else:
                self.x = 10

    def fire(self):
        # if self.direct == Direct.UP:
        #     bullet = Bullet(self.x + 14, self.y - 14, direct=Direct.UP)
        # elif self.direct == Direct.RIGHT:
        #     bullet = Bullet(self.x + 40, self.y + 14, direct=Direct.RIGHT)
        # elif self.direct == Direct.DOWN:
        #     bullet = Bullet(self.x + 14, self.y + 40, direct=Direct.DOWN)
        # elif self.direct == Direct.LEFT:
        #     bullet = Bullet(self.x - 10, self.y + 14, direct=Direct.LEFT)
        # return bullet
        if self.direct == Direct.UP:
            x, y = self.x + 14, self.y - 14
        elif self.direct == Direct.RIGHT:
            x, y = self.x + 40, self.y + 14
        elif self.direct == Direct.DOWN:
            x, y = self.x + 14, self.y + 40
        elif self.direct == Direct.LEFT:
            x, y = self.x - 10, self.y + 14
        return Bullet(x, y, direct=self.direct)

    def draw(self, screen):
        # 坦克主体
        pygame.draw.rect(screen, self.color, (self.x,self.y, 30, 30), 0)

        # 坦克履带
        if self.direct == Direct.UP or self.direct == Direct.DOWN:
            pygame.draw.rect(screen, self.color, (self.x - 10, self.y - 10, 10, 50), 0)
            pygame.draw.rect(screen, self.color, (self.x + 30, self.y - 10, 10, 50), 0)
        else:
            pygame.draw.rect(screen, self.color, (self.x - 10, self.y - 10, 50, 10), 0)
            pygame.draw.rect(screen, self.color, (self.x - 10, self.y + 30, 50, 10), 0)

        # 坦克炮管
        if self.direct == Direct.UP:
            pygame.draw.line(screen, black_color, (self.x + 13, self.y + 15), (self.x + 13, self.y - 10), 4)
        elif self.direct == Direct.RIGHT:
            pygame.draw.line(screen, black_color, (self.x + 15, self.y + 13), (self.x + 40, self.y + 13), 4)
        elif self.direct == Direct.DOWN:
            pygame.draw.line(screen, black_color, (self.x + 13, self.y + 15), (self.x + 13, self.y + 40), 4)
        elif self.direct == Direct.LEFT:
            pygame.draw.line(screen, black_color, (self.x - 10, self.y + 13), (self.x + 15, self.y + 13), 4)


# python 搜索一个变量的方式是LEGB -->  local  Embedded  Global  Built-in
def main():

    def refresh_screen():
        pygame.draw.rect(screen, bg_color, (0, 0, 800, 600), 0)
        mytank.draw(screen)
        for e in enemy_list:
            e.draw(screen)
        for b in bullet_list:
            b.draw(screen)
        pygame.display.flip()

    pygame.init()

    screen = pygame.display.set_mode((800, 600))  # 设置窗口大小
    pygame.display.set_caption('坦克大战')  # 设置窗口标题

    # rect(container, bg_color, position, line) 画矩形  container 容器 bg_color 背景色 position 位置，一个元组 line 线的粗细
    # pygame.draw.rect(screen, bg_color, (0, 0, 800, 600), 0)

    # 画坦克
    x, y = 365, 555
    mytank = Tank(x, y, direct=Direct.UP)
    # tank.draw(screen)
    # pygame.display.flip()  # 渲染窗口

    enemy_list = []
    for i in range(5):
        enemy = Tank(i * 180 + 10, 10, color=red_color, direct=Direct.DOWN)
        enemy_list.append(enemy)
    bullet_list = []

    running = True
    while running:
        sleep(0.07)
        mytank.move()

        for b in bullet_list:
            b.fly()

        refresh_screen()

        for event in pygame.event.get():  # pygame.event.get() 获取pygame所有的事件对象
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:  # 上
                    mytank.direct = Direct.UP
                    mytank.move()
                elif event.key == pygame.K_a:  # 左
                    mytank.direct = Direct.LEFT
                    mytank.move()
                elif event.key == pygame.K_s:  # 下
                    mytank.direct = Direct.DOWN
                    mytank.move()
                elif event.key == pygame.K_d:  # 右
                    mytank.direct = Direct.RIGHT
                    mytank.move()
                elif event.key == pygame.K_SPACE:  # 空格
                    if len(bullet_list) < 5:
                        bullet_list.append(mytank.fire())

        for b in bullet_list:
            if b.x == 0 or b.x == 800 or b.y == 0 or b.y == 600:
                bullet_list.remove(b)
            # for e in enemy_list:
            #     if (b.x + 4 < e.x - 10 and b.y < ) or b.x > e.x + 40 or b.y + 4 < e.y - 10 or b.y > e.y + 40:
            #         print(111)

    pygame.quit()


if __name__ == '__main__':
    main()

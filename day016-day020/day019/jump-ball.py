from time import sleep

import pygame


class Ball(object):
    def __init__(self, x, y, speedx=5, speedy=5, color=(255, 0, 0)):
        self.x = x
        self.y = y
        self.speedx = speedx
        self.speedy = speedy
        self.color = color

    def move(self):
        if self.x - 20 <= 0 or self.x + 20 >= 800:
            self.speedx = -self.speedx
        if self.y - 20 <= 0:
            self.speedy = -self.speedy
        if self.x - 20 >= 0 and self.x + 20 <= 800 and self.y + 20 >= 600:
            pass
        self.x += self.speedx
        self.y += self.speedy

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), 20, 0)


class Board(object):
    def __init__(self, x, y, height, weight, speed=10):
        self.x = x
        self.y = y
        self.height = height
        self.weight = weight
        self.speed = speed

    def move(self, direct):
        if direct == 1:
            self.x -= self.speed
        elif direct == -1:
            self.x += self.speed

        if self.x <= 0:
            self.x = 0
        elif self.x + self.weight >= 800:
            self.x = 800 - self.weight

    def draw(self, screen):
        pygame.draw.rect(screen, (0, 0, 255), (self.x, self.y, self.weight, self.height), 0)


def main():
    def refresh_screen():
        pygame.draw.rect(screen, (242, 242, 242), (0, 0, 800, 600), 0)
        ball.draw(screen)
        board.draw(screen)
        pygame.display.flip()

    pygame.init()

    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption('跳跳球')

    pygame.draw.rect(screen, (255, 0, 0), (0, 0, 800, 600), 0)

    ball = Ball(50, 50, 5, 5)
    board = Board(360, 590, 10, 80)

    running = True
    while running:
        sleep(0.05)

        ball.move()

        refresh_screen()

        for event in pygame.event.get():  # pygame.event.get() 获取pygame所有的事件对象
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    board.move(direct=1)
                elif event.key == pygame.K_RIGHT:
                    board.move(direct=-1)

        if (ball.x >= board.x and ball.x <= board.x + 80) and ball.y + 20 >= board.y:
            ball.speedy = -ball.speedy

    pygame.quit()


if __name__ == '__main__':
    main()

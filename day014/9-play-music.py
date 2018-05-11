import pygame
import time

def playMusic(path):
    # 初始化pygame
    pygame.mixer.init()
    # 加载音乐
    pygame.mixer.music.load(path)
    # 播放
    pygame.mixer.music.play()

for i in range(5):
    path = r'./music/'+str(i)+'.mp3'
    playMusic(path)
    time.sleep(10)
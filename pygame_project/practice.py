import os
import pygame

current_path = os.path.dirname(__file__) # 현재 파일의 위치 반환
image_path = os.path.join(current_path, "images") # images 폴더 위치 반환

# 배경 만들기
background = pygame.image.load(os.path.join(image_path, "background.png"))

a = background.get_rect()

a.left = 1
a.top = 2
a.size = (330,400)

print(a)
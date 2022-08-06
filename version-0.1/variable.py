import pygame
import sys

pygame.init()
SCREEN_W = 350
SCREEN_H = 650
SCREEN = pygame.display.set_mode((SCREEN_W, SCREEN_H))

StartButton_W = 100
StartButton_H = 100
StartButton_X = SCREEN_W / 2 - StartButton_W / 2
StartButton_Y = SCREEN_H / 2 + StartButton_H

img_StartButton = pygame.image.load("image\StartButton.png")
img_StartButton = pygame.transform.scale(img_StartButton,(StartButton_W, StartButton_H)) # 지도 크기 조절

main_font = pygame.font.SysFont("휴먼옛체", 20)
start_text = main_font.render("시작하기",True,(200,200,200))
start_text_X = StartButton_X + StartButton_W / 6
start_text_Y = StartButton_Y + 100


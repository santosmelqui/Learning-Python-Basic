'''Faça um programa em Python que abra e erproduza o áudio de
 um arquivo mp3'''

import pygame

pygame.init()
pygame.mixer.music.load('audio.mp3')
pygame.mixer.music.play()
input()
pygame.event.music.stop()
pygame.quit()




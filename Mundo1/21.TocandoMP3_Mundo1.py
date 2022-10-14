#Exercício Python 21: Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.

import pygame
pygame.init()
pygame.mixer.music.load("nome do meu arquivo de musica")
pygame.mixer.music.play()
pygame.event.wait()
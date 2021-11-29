# Faça um programa em python que abra e repruzir o audio de um arquivo MP3.


import pygame # esse modulos tem funcionalidades para criar jogos ...
pygame.init()  #iniciar o pygame
pygame.mixer.music.load ('ex021.mp3') #mixer do pygame carrega a musica
pygame.mixer.music.play() # da o play
pygame.event.wait() # esse comando espera o evento acabar

''' biblioteca pygame estudar'''
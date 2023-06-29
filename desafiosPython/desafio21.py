import pygame

#inicializando pygame
pygame.init()

#inicializando mixer de audio
pygame.mixer.init()

#carregar arquivo MP3
pygame.mixer.music.load("audio.mp3")

#reproduzir arquivo MP3
pygame.mixer.music.play()

#aguarda até a musica acabar
while pygame.mixer.music.get_busy():
    continue

#encerra o pygame
pygame.quit()


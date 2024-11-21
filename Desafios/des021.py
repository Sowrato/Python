import pygame

print('\n','-'*5,'DESAFIO 021','-'*5,'\n')

pygame.init()

pygame.mixer.music.load('rap-hashirama.mp3')

pygame.mixer.music.play()

pygame.event.wait()

print('\n','-'*5,'FIM DO PROGRAMA','-'*5,'\n')
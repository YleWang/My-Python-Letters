import pygame
pygame.init()
screen=pygame.display.set_mode((480,480))


while True:
                for i in pygame.event.get():
                                if i.type==pygame.QUIT:
                                                pygame.quit()

                screen.fill((0,255,0))
                pygame.draw.rect(screen,(255,0,0),(160,160,160,160))
                pygame.display.update()

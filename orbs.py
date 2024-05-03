import pygame
from Camera import camera
import random

class orb:
    def __init__(self,x,y,h,w):
        self.rect=pygame.Rect(x,y,h,w)
        image=pygame.image.load("C.png")
        self.texture=pygame.transform.scale(image,(h,w))

    def update(self,fruit,fruits_list,player):
        if self.rect.colliderect(player.rect):
            player.score += 5
            fruits_list.remove(fruit)

    def draw(self,window,camera):
        window.blit(self.texture,(camera.translate(self.rect.x,self.rect.y)))
    


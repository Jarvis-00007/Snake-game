import pygame

class Segment:
    def  __init__(self,x,y,w,h,fpath):
        self.rect=pygame.Rect(x,y,w,h)
        img=pygame.image.load("reddot.png")
        self.texture=pygame.transform.scale(img,(w,h))
        self.speed=1
    
    def update(self,target):
         direction=[target[0]-self.rect.x,target[1]-self.rect.y]
         length=(direction[0]**2 +direction[1]**2)**(1/2)
         if length<self.rect.w/2:
             return
         direction[0] /= length
         direction[1] /= length

         self.rect.x += direction[0] *self.speed
         self.rect.y += direction[1] * self.speed


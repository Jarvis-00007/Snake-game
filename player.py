import pygame
from segment import Segment

class Player:
    def __init__(self,x,y,w,h,fpath):
        self.speed=1
        self.rect=pygame.Rect(x,y,w,h)
        img=pygame.image.load("reddot.png")
        self.texture=pygame.transform.scale(img,(w,h))
        self.pscore=0
        self.score=0
        self.segments=[]

    def draw(self,window,camera):
        window.blit(self.texture,camera.translate(self.rect.x,self.rect.y))
        
        for seg in self.segments:
           window.blit(seg.texture,camera.translate(seg.rect.x,seg.rect.y)) 


    def play(self):
        pass

    def update(self,windims):
        mouse_pos=pygame.mouse.get_pos()
        world_pos=((mouse_pos[0]-windims[0]/2,mouse_pos[1]-windims[1]/2))
        print(mouse_pos)
        length=((mouse_pos[0]-windims[0]/2)**2+(mouse_pos[1]-windims[1]/2)**2)**0.5
        self.rect.x+=(world_pos[0]/length)*self.speed
        self.rect.y+=(world_pos[1]/length)*self.speed
        dirV=[(world_pos[0]-self.rect.x)/length,(world_pos[1]-self.rect.y)/length,]
        
        if(self.score-self.pscore==20):
            self.pscore=self.score
            
            startX=dirV[0]*-1*self.rect.w+self.rect.x
            startY=dirV[1]*-1*self.rect.h+self.rect.y
            newSegment=Segment(startX,startY,self.rect.w,self.rect.h,"reddot.png")
            self.segments.append(newSegment)

        for i in range(len(self.segments)):
            if i==0:
                self.segments[i].update((self.rect.x,self.rect.y))
            else:
                self.segments[i].update((self.segments[i-1].rect.x,self.segments[i-1].rect.y))



    def render(self):
        pass

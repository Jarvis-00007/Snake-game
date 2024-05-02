import pygame
class Player:
    def __init__(self,x,y,w,h):
        self.speed=1
        self.rect=pygame.Rect(x,y,w,h)
        img=pygame.image.load("reddot.png")
        self.texture=pygame.transform.scale(img,(w,h))

    def draw(self,window,camera):
        window.blit(self.texture,camera.translate(self.rect.x,self.rect.y))

    def play(self):
        pass

    def update(self,windims):
        mouse_pos=pygame.mouse.get_pos()
        world_pos=((mouse_pos[0]-windims[0]/2,mouse_pos[1]-windims[1]/2))
        print(mouse_pos)
        length=((mouse_pos[0]-windims[0]/2)**2+(mouse_pos[1]-windims[1]/2)**2)**0.5
        self.rect.x+=(world_pos[0]/length)*self.speed
        self.rect.y+=(world_pos[1]/length)*self.speed
        pass
    def render(self):
        pass

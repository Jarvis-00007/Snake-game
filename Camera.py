import pygame
class camera:
    def __init__(self,x,y,playerdims,windims):
        self.playerdims=playerdims
        self.windims=windims
        self.x=x
        self.y=y
    def update(self,player_x,player_y):
        self.x=player_x
        self.y=player_y
    def translate(self,orb_x,orb_y):
        return (orb_x-self.x+self.windims[0]/2-self.playerdims[0]/2,
                orb_y-self.y+self.windims[1]/2-self.playerdims[1]/2)

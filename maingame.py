from orbs import orb
from player import Player
import pygame
import random
from Camera import camera

pygame.init()
num_orbs=10
startw=50
starth=50
clock=pygame.time.Clock()

class maingame:
  def __init__(self,pl_data):
    self.dims=(1000,700)
    self.loop=False
    self.window=pygame.display.set_mode(self.dims)
    self.orbs=[]
    self.camera=camera(self.dims[0]/2-startw/2,self.dims[1]/2-starth/2,(starth,startw),self.dims)
    print(pl_data)
    self.player=pl_data
    self.init()

  def init(self):
    for i in range(num_orbs):
      randX=random.randint(0,self.dims[0]+1000)
      randY=random.randint(0,self.dims[1]+1000)
      randr=50
      fruit=orb(randX,randY,randr,randr)
      self.orbs.append(fruit)
    self.play()

  def update(self):
    for event in pygame.event.get():
      if event.type==pygame.QUIT:
        self.loop=True
    self.player.update(self.dims)
    for fruit in self.orbs:
      fruit.update(fruit,self.orbs,self.player)
    self.camera.update(self.player.rect.x,self.player.rect.y)

  def render(self):
    self.window.fill((48,25,52))
    for fruit in self.orbs:
      fruit.draw(self.window,self.camera)
    self.player.draw(self.window,self.camera)
    pygame.display.update()
   

  def play(self):
    while not self.loop:
      clock.tick(200)
      self.update()
      self.render()

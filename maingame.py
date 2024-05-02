from orbs import orb
from player import player
import pygame
import random

pygame.init()
num_orbs=30
startw=50
starth=50

class maingame:
  def __init__(self):
    self.dims=(1000,500)
    self.loop=False
    self.window=pygame.display.set_mode(self.dims)
    self.orbs=[]
    
    self.player=Player(0,0,startw,starth)

  def init(self):
    for i in range(num_orbs):
      randX=random.randint(0,self.dims[0])
      randY=random.randint(0,self.dims[1])
      randr=random.randint(0,50)
      fruit=orb(randX,randY,randr,randr)
      self.orbs.append(fruit)
    self.play()
  def update(self):
    for event in pygame.event.get():
      if event.type==pygame.QUIT:
        self.loop=True


  def render(self):
    self.window.fill((48,25,52))
    for fruit in self.orbs:
      fruit.draw(self.window)
    self.player.draw(self.window)
    pygame.display.update()
   

  def play(self):
    while not self.loop:
      self.update()
      self.render()

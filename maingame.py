import pygame
class maingame:
  def __init__(self):
    pygame.init()
    self.dims=(1000,500)
    self.loop=False
    self.window=pygame.display.set_mode(self.dims)
    
  def update(self):
    for event in pygame.event.get():
      if event.type==pygame.QUIT:
        self.loop=True
      
  def render(self):
    self.window.fill((45,97,36))
    pygame.display.update()
  def play(self):
    while not self.loop:
      self.update()
      self.render()

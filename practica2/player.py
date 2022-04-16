import multiprocessing.connection import client
import traceback
import pygame
import sys, os

HEIGHT=400
WIDTH=800

PLAYER_ONE=0
PLAYER_TWO=1
PLAYER_THREE=2

SIDESSTR = ["left","centre","right"]
SIDES=["left","right"]
#SIDESSTR=["left","rigth"]

##################################################

class Rabbit():
  def __init__(self,side)
    self.side=side
    self.pos=[None,None]
    
  def get_pos(self):
    return self.pos
  
  def get_side(self):
    return self.side
  
  def set_pos(self,pos):
    self.pos=pos
    
   def __str__(self):
    return f"P<{SIDES[self.side],self.pos}>"
  
##################################################

class Car1():

    def __init__(self,n):
        self.pos=[None,None]
    
    def get_pos(self):
        return self.pos
      
    def set_pos(self,pos):
        self.pos=pos
      
    def __str__(self):
        return f"C<self.pos>"
      
################################################## 
 
class Car2():

    def __init__(self,n):
        self.pos=[None,None]
    
    def get_pos(self):
        return self.pos
      
    def set_pos(self,pos):
        self.pos=pos
      
    def __str__(self):
        return f"C<self.pos>"
      
##################################################  
  
class Car3():
  
    def __init__(self,n):
        self.pos=[None,None]
    
    def get_pos(self):
        return self.pos
      
    def set_pos(self,pos):
        self.pos=pos
      
    def __str__(self):
        return f"C<self.pos>"
      
##################################################

class Game():
  def __init(self):
    self.players=[Player(i) for i in range(3)]
    self.car1=[Car1(i) for i in range(2)]
    self.car2=[Car2(i) for i in range(2)]
    self.car3=[Car3(i) for i in range(2)]
    self.running=True
  
  def get_rabbit(self,side):
    return self.rabbit[size]
    
  def set_pos_rabbit(self,side,pos):
    self.rabbit[side].set_pos(pos)
    
  def get_car1(self,i):
    return self.car1[i]
  
  def set_pos_car1(self,i,pos):
    self.car1[i].set_pos(pos)
  
  def get_car2(self,i):
    return self.car2[i]
 
  def set_pos_car2(self,i,pos):
    self.car2[i].set_pos(pos)
    
  def get_car3(self,i):
    return self.car3[i]

  def set_pos_car3(self,i,pos):
    self.car3[i].set_pos(pos)
    
  def update(self,gameinfo):
    self.set_pos_rabbit(PLAYER_ONE,gameinfo['pos_player_one']
    self.set_pos_rabbit(PLAYER_TWO,gameinfo['pos_player_two']
    self.set_pos_rabbit(PLAYER_THREE,gameinfo['pos_player_three']
    info_car1=gameinfo['pos_car1']
    info_car2=gameinfo['pos_car2']
    info_car3=gameinfo['pos_car3']
    for i in range(2):
      Car1_i=info_car1[i]
      self.set_pos_car1(i,Car1_i)
    for i in range(2):
      Car2_i=info_car2[i]
      self.set_pos_car2(i,Car2_i)
    for i in range(2):
      Car3_i=info_car3[i]
      self.set_pos_car3(i,Car3_i)  
    self.running=gameinfo['is running']
                       
  def is_running(self):
    return self.running
   
  def finish(self):
    self.running=False
              
  def __str__(self:
    for i in range(2):
      return f"G<{self.rabbit[PLAYER_ONE]}:{self.rabbit[PLAYER_TWO]}:{self.rabbit[PLAYER_THREE]}:{self.car1[i]}>"
    for i in range(2):
      return f"G<{self.rabbit[PLAYER_ONE]}:{self.rabbit[PLAYER_TWO]}:{self.rabbit[PLAYER_THREE]}:{self.car2[i]}>"
    for i in range(2):
      return f"G<{self.rabbit[PLAYER_ONE]}:{self.rabbit[PLAYER_TWO]}:{self.rabbit[PLAYER_THREE]}:{self.car3[i]}>"

##################################################
              
class Rabbit_Draw(pygame.sprite.Sprite):
    
    def __init__(self,mon,ind):
        super().__init__()
        self.rabbit = rab
        self.index = ind
        self.image = pygame.image.load(f'conejo{self.index}.png')
        self.image = pygame.transform.scale(self.image,(70,70))
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.update()
        
    def update(self):        
        pos = self.rabbit.get_pos()
        self.rect.centerx, self.rect.centery = pos  
        
    def draw(self, screen):
        screen.window.blit(self.image, self.rect)
   
    def __str__(self):
        return f"S<{self.rab}>"

##################################################
              
class Car1_Draw(pygame.sprite.Sprite):
    
    def __init__(self, car1):
        super().__init__()
        self.car1 = car1
        self.image= pygame.image.load(f'coche1.png')
        self.image = pygame.transform.scale(self.image,(70,50))
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.update()

    def update(self):
        pos = self.car1.get_pos()
        self.rect.centerx, self.rect.centery = pos
        
    def draw(self,screen):
        screen.window.blit(self.image,(self.ball.pos))
       
    def __str__(self):
        return f"P<{self.car1.pos}>"
              
##################################################

class Car2_Draw(pygame.sprite.Sprite):
    
    def __init__(self, car2):
        super().__init__()
        self.car2 = car2
        self.image= pygame.image.load(f'coche2.png')
        self.image = pygame.transform.scale(self.image,(70,50))
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.update()

    def update(self):
        pos = self.car2.get_pos()
        self.rect.centerx, self.rect.centery = pos
        
    def draw(self,screen):
        screen.window.blit(self.image,(self.ball.pos))
       
    def __str__(self):
        return f"P<{self.car2.pos}>"
              
##################################################

class Car3_Draw(pygame.sprite.Sprite):
    
    def __init__(self, car3):
        super().__init__()
        self.car3 = car3
        self.image= pygame.image.load(f'coche3.png')
        self.image = pygame.transform.scale(self.image,(70,50))
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.update()

    def update(self):
        pos = self.car3.get_pos()
        self.rect.centerx, self.rect.centery = pos
        
    def draw(self,screen):
        screen.window.blit(self.image,(self.ball.pos))
       
    def __str__(self):
        return f"P<{self.car3.pos}>"              

##################################################        

class Display(): #SIN TERMINAR
    
    def __init__(self, game):        
        self.game = game
        self.score = game.get_score()
        self.rabbitD = [Rabbit_Draw(self.game.get_monkey(i),i+1) for i in range(3)]
        self.carD = [Car_Draw(self.game.get_banana(i)) for i in range(3)]
        self.all_sprites = pygame.sprite.Group()
        self.rabbit_group = pygame.sprite.Group()
        self.bcar_group = pygame.sprite.Group()
        for rabbit in self.rabbitD:
            self.all_sprites.add(rabbit)
            self.rabbit_group.add(rabbit)
        for banana in self.bananaD:
            self.all_sprites.add(banana)
            self.banana_group.add(banana)
        self.screen = pygame.display.set_mode(SIZE)
        self.clock =  pygame.time.Clock()  #FPS
        self.background = pygame.image.load('road.jpg')
        self.background = pygame.transform.scale(self.background,(WIDTH,HEIGHT))
        pygame.init()
     
    def analyze_events(self, side):        
        events = []        
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    events.append("quit")
                elif event.key == pygame.K_DOWN:
                    events.append("down")
                elif event.key == pygame.K_UP:
                    events.append("up")
            elif event.type == pygame.QUIT:
                events.append("quit")        
        #if pygame.sprite.groupcollide(self.rabbitD,self.carD,False,False):            
        if pygame.sprite.spritecollideany(self.rabbitD[0],self.carD):
            events.append("collideleft")            
        if pygame.sprite.spritecollideany(self.rabbitD[1],self.carD):
           events.append("collideright")                     
        return events

    def refresh(self):
       self.all_sprites.update()
       self.screen.blit(self.background,(0,0))
       pos=self.rabbit.get_pos()
           if pos[0]==0 or pos[1]==0 or pos[2]==0:
              font2=pygame.font.Font(None,100)
              text1=font2.render(f"GAME OVER",1,(255,0,0))
              self.screen.blit(text1,(150,250))
       self.all_sprites.draw(self.screen)
       pygame.display.flip()
              
    def tick(self):
        self.clock.tick(FPS)

    @staticmethod
    def quit():
        pygame.quit()

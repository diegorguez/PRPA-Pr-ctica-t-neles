from multiprocessing.connection import Client
import traceback
import pygame
import sys, os

HEIGHT=800
WIDTH=800

PLAYER_ONE=0
PLAYER_TWO=1
PLAYER_THREE=2

SIDESSTR = ["left","centre","right"]
SIDES=["down","up"]

FPS = 60

##################################################

class Player():
    def __init__(self,side):
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

class Car():

    def __init__(self,n):
        self.pos=[None,None,None]
        self.divider = n
    
    def get_pos(self):
        return self.pos
    
    def get_index(self):
        return self.divider
          
    def set_pos(self,pos):
        self.pos=pos
      
    def __str__(self):
        return f"C<self.pos>"
    
##################################################

class Game():
    def __init__(self):
        self.players=[Player(i) for i in range(3)]
        self.car=[Car(i) for i in range(3)]
        self.running=True
  
    def get_rabbit(self,side):
        return self.players[side]
    
    def set_pos_rabbit(self,side,pos):
        self.players[side].set_pos(pos)
    
    def get_car(self,i):
        return self.car[i]
  
    def set_pos_car(self,i,pos):
        self.car[i].set_pos(pos)
    
    def update(self, gameinfo):
        self.set_pos_rabbit(PLAYER_ONE, gameinfo['pos_player_one'])
        self.set_pos_rabbit(PLAYER_TWO, gameinfo['pos_player_two'])
        self.set_pos_rabbit(PLAYER_THREE, gameinfo['pos_player_three'])
        info_car=gameinfo['pos_cars']
        for i in range(3):
            Car_i=info_car[i]
            self.set_pos_car(i,Car_i)  
        self.running=gameinfo['is_running']
                       
    def is_running(self):
        return self.running
   
    def finish(self):
        self.running=False
         
    def __str__(self):
        for i in range(3):
            return f"G<{self.players[PLAYER_TWO]}:{self.players[PLAYER_ONE]}:{self.car[i]}"

##################################################
              
class Rabbit_Draw(pygame.sprite.Sprite):
    
    def __init__(self,rab,ind):
        super().__init__()
        self.rabbit = rab
        self.index = ind
        self.image = pygame.image.load(f'conejo{self.index}.png')
        self.image = pygame.transform.scale(self.image,(70,70))
        self.image.set_colorkey((255, 255, 255))
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
              
class Car_Draw(pygame.sprite.Sprite):
    
    def __init__(self, car):
        super().__init__()
        self.car = car
        n = self.car.get_index()
        self.image= pygame.image.load(f'coche{n+1}.png')
        self.image = pygame.transform.scale(self.image,(70,50))
        self.image.set_colorkey((255, 255, 255))
        self.rect = self.image.get_rect()
        self.update()

    def update(self):
        pos = self.car.get_pos()
        self.rect.centerx, self.rect.centery = pos
        
    def draw(self,screen):
        screen.window.blit(self.image,(self.ball.pos))
       
    def __str__(self):
        return f"P<{self.car.pos}>"              

##################################################        

class Display():
    
    def __init__(self, game):        
        self.game = game
        self.rabbits = [self.game.get_rabbit(i) for i in range(3)]
        self.rabbitD = [Rabbit_Draw(self.game.get_rabbit(i),i+1) for i in range(3)]
        self.carD = [Car_Draw(self.game.get_car(i)) for i in range(3)]
        self.all_sprites = pygame.sprite.Group()
        self.rabbit_group = pygame.sprite.Group()
        self.car_group = pygame.sprite.Group()
        for rabbit in self.rabbitD:
            self.all_sprites.add(rabbit)
            self.rabbit_group.add(rabbit)
        for car in self.carD:
            self.all_sprites.add(car)
            self.car_group.add(car)
        self.screen = pygame.display.set_mode((WIDTH,HEIGHT))
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
        
        if pygame.sprite.spritecollideany(self.rabbitD[0],self.carD):
            events.append("firstcollide")
            
        if pygame.sprite.spritecollideany(self.rabbitD[1],self.carD):
           events.append("secondcollide") 
                         
        if pygame.sprite.spritecollideany(self.rabbitD[2],self.carD):
           events.append("thirdcollide")    
                              
        return events

    def refresh(self):
        self.all_sprites.update()
        self.screen.blit(self.background, (0,0))
        font = pygame.font.Font(None, 74)
        aux = False
        
        if self.rabbits[0].pos[1] <= 0:
            font2 = pygame.font.Font(None,50) 
            text1 = font2.render(f"PLAYER 1 WINS!", 1, RED)
            self.screen.blit(text1, (45, 150))
            aux = True
        if self.rabbits[1].pos[1] <= 0:
            font2 = pygame.font.Font(None,50) 
            text1 = font2.render(f"PLAYER 2 WINS!", 1, RED)
            self.screen.blit(text1, (45, 150))
            aux = True
        if self.rabbits[2].pos[1] <= 0:
            font2 = pygame.font.Font(None,50) 
            text1 = font2.render(f"PLAYER 3 WINS!", 1, RED)
            self.screen.blit(text1, (45, 150))
            aux = True
        self.all_sprites.draw(self.screen)
        pygame.display.flip()
        if aux:
            time.sleep(6)     
    def tick(self):
        self.clock.tick(FPS)

    @staticmethod
    def quit():
        pygame.quit()
                
##################################################                 
                
def main(ip_address):

    try:
        with Client((ip_address, 6000), authkey=b'secret password') as conn:
            game = Game()
            side,gameinfo = conn.recv()
            print(f"I am playing {SIDESSTR[side]}")
            game.update(gameinfo)
            display = Display(game)
            while game.is_running():
                events = display.analyze_events(side)
                for ev in events:
                    conn.send(ev)
                    if ev == 'quit':
                        game.finish()
                conn.send("next")
                gameinfo = conn.recv()
                game.update(gameinfo)
                display.refresh()
                display.tick()
    except:
        traceback.print_exc()
    finally:
        pygame.quit()
                
        
if __name__=="__main__":
    ip_address="127.0.0.1"
    if len(sys.argv)>1:
        ip_address=sys.argv[1]
    main(ip_address)

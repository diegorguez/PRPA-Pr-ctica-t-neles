from multiprocessing.connection import Listener
from multiprocessing import Process, Manager, Value, Lock
import traceback
import sys
import random as rd

HEIGHT=400
WIDTH=600
PLAYER_ONE=0
PLAYER_TWO=1
PLAYER_THREE=2
MOVEMENT=20

class Player():
  def __init__(self,side):
    self.side=side
    if side==PLAYER_ONE
      self.pos=[WIDHT/4,0]
      #self.pos=[WIDHT/4,HEIGHT]
    if side==PLAYER_TWO
      self.pos=[WIDTH/2,0]
      #self.pos=[WIDTH/2,HEIGHT]
    if side==PLAYER_THREE
      self.pos=[3*WIDTH/4,0]
      #self.pos=[3*WIDTH/4,HEIGHT]
  
  def get_pos(self):
    return self.pos
  
  def get_side(self):
    return self.side
 
  def moveDown(self):
    self.pos[1]+=MOVEMENT
    if self.pos[1]>HEIGHT:
      self.pos[1]=HEIGHT
  
  def moveUP(self):
    self.pos[1]+=MOVEMENT
    #self.pos[1]-=MOVEMENT
    if self.pos[1]<0:
      self.pos[1]=0
      
  def __str__(self):
    return f"P<{SIDESSTR[self.side]},{self.pos}>"
      
  
class Car1():
  def __init__(self,index):
    self.x = rd.randint(-1000,-1) #Colocamos los cohces1 a la izquierda de form aleatoria
    list = [100,300,500]           
    self.y = random.choice(list)
    self.pos = [self.x , self.y]
    self.vel = random.randint(8,20) 
    
    def get_pos(self):
        return self.pos         
        
    def update(self):        
        self.pos[Y] = self.pos[Y] 
        self.pos[X] += self.vel  
     
    def __str__(self):
        return f"B<{self.pos}>"
  
class Car2():
  
class Car3():
  
class Game():
  
def player(side,conn,game):
  try:
    print(f"starting player {SIDESSTR[side]}:{game.get_info()}")
    conn.send_((side,game.get:info()))
    while game.is_running():
      command=""
      while command != "next":
        command=conn.recv()
        if command=="up":
          game.moveUp(side)
        elif command=="down":
          game.moveDown(side)
  except:
    traceback.print_exc()
    conn.close()
  finally:
    print(f"Game ended {game}")
    
def main(ip_adrress):
  manager=Manager()
  try:
    with Listener((ip_address,6000),authkey=b'secret pasword?) as listener:
      n_player=0
      players=[None,None,None]
      game=Game(manager)
      while True:
        print(f"accepting connection {n_player}")
        conn=listener.accept()
        players{n_player}=Process(target=player,args=(n_player,conn,game))
        n_player+=1
        if n_player==3:
          players[0].start()
          players[1].start()
          players[2].start()
          n_player=0
          players=[None,None,None]
          game=Game(manager)
  except Exceotion as e:
    traceback.print_exc()
                    
  
  
if __name__=='__main__':
  
  
         

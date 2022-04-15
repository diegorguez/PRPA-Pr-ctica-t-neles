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
  #clase de los conejos, para indicar su tamaño, su posición y sus movimientos
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
  #Clase de los coches que van de izquierda a derecha, indicando su tamaño, su posición y sus movimientos.
  def __init__(self,index):
    self.x = rd.randint(-10000,-1) #los situamos a la izquierda de la pantalla a mayor o menor distancia de ella, para que su aparicion en el juego sea en distinto instante
    list = [100,500]   #La altura 100 se coresponde con el carril superior, y la altura 500 con el inferior       
    self.y = random.choice(list)
    self.pos = [self.x , self.y]
    self.vel = random.randint(8,20) 
    
    def get_pos(self):
        return self.pos         
        
    def update(self): #con la función update (el paso de los frames del juego) indicamos que los coches solo se moverán en el eje horizontal        
        self.pos[Y] = self.pos[Y] 
        self.pos[X] += self.vel  
     
    def __str__(self):
        return f"B<{self.pos}>"
  
class Car2(): #Coches que van de derecha a izquierda
  def __init__(self,index):
    self.x = rd.randint(800,10800) #los situamos a la derecha de la pantalla a mayor o menor distancia de ella, para que su aparicion en el juego sea en distinto instante       
    self.y = 300   #la altura 300 se corresponde con el carril central
    self.pos = [self.x , self.y]
    self.vel = random.randint(8,20) 
    
    def get_pos(self):
        return self.pos         
        
    def update(self): #con la función update (el paso de los frames del juego) indicamos que los coches solo se moverán en el eje horizontal        
        self.pos[Y] = self.pos[Y] 
        self.pos[X] += self.vel  
     
    def __str__(self):
        return f"B<{self.pos}>"
  
  
class Game():
  
  
  
def player(side,conn,game):
  try:
    print(f"starting player {SIDESSTR[side]}:{game.get_info()}")
    conn.send_((side,game.get:info()))
    while game.is_running():
      command=""
      while command != "next":
        command=conn.recv()
        if command=="up": #para que la tecla "up" haga que avance el conejo
          game.moveUp(side)
        elif command=="down": #para que la tecla "down" haga que retroceda el conejo
          game.moveDown(side)
        elif command=="collideone": #para cuando el conejo 1 se choque con algún coche
          #codigo (aplicacion en clase game)
        elif command=="collidetwo": #para cuando el conejo 2 se choque con algún coche
          #codigo (aplicacion en clase game)
        elif command=="collidethree": #para cuando el conejo 3 se choque con algún coche
          #codigo (aplicacion en clase game)
          
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
  ip_address="127.0.0.1"
  if len/sys.argv)>1:
    ip_address=sys.argv[1]
      
  main(ip_address)
  
         

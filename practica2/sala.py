"""Aplicación distribuida: Juego: Cruzar la carretera
   Alejandro Cruz
   Pablo Mollá
   Diego Rodríguez
   Pablo Sánchez"""

from multiprocessing.connection import Listener
from multiprocessing import Process, Manager, Value, Lock
import traceback
import sys
import random as rd

HEIGHT=400
WIDTH=800
PLAYER_ONE=0
PLAYER_TWO=1
PLAYER_THREE=2
MOVEMENT=20

X = 0
Y = 1


class Conejo():
#clase de los conejos, para indicar su tamaño, su posición y sus movimientos
    def __init__(self,side):
        self.side=side
        if side==PLAYER_ONE:
            self.pos=[WIDHT/4,0]
            #self.pos=[WIDHT/4,HEIGHT-30]
        if side==PLAYER_TWO:
            self.pos=[WIDTH/2,0]
            #self.pos=[WIDTH/2,HEIGHT-30]
        if side==PLAYER_THREE:
            self.pos=[3*WIDTH/4,0]
            #self.pos=[3*WIDTH/4,HEIGHT-30]
  
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
  
    def reiniciar_P(self):
        self.pos[1]=0
      
    def __str__(self):
        return f"P<{SIDESSTR[self.side]},{self.pos}>"
      

  
class Car1():
#Clase de los coches del carril superior, indicando su tamaño, su posición y sus movimientos.
    def __init__(self,index):
        self.x = rd.randint(-10000,-1) #los situamos a la izquierda de la pantalla a mayor o menor distancia de ella, para que su aparicion en el juego sea en distinto instante  
        self.y = 100  #La altura 100 se coresponde con el carril superior
        self.pos = [self.x , self.y]
        self.vel = random.randint(8,20) 
    
    def get_pos(self):
        return self.pos         
        
    def update(self): #con la función update (el paso de los frames del juego) indicamos que los coches solo se moverán en el eje horizontal        
        self.pos[Y] = self.pos[Y] 
        self.pos[X] += self.vel  
     
    def __str__(self):
        return f"B<{self.pos}>"
  
  
  
class Car2():
#Clase de los coches que van por el carril medio, de derecha a izquierda, indicando su tamaño, su posición y sus movimientos.
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
  
 
  
class Car3():
#Clase de los coches del carril superior, de izquierda a derecha, indicando su tamaño, su posición y sus movimientos.
    def __init__(self,index):
        self.x = rd.randint(-10000,-1) #los situamos a la izquierda de la pantalla a mayor o menor distancia de ella, para que su aparicion en el juego sea en distinto instante  
        self.y = 500  #La altura 500 se coresponde con el carril inferior
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
  
    def __init__(self, manager):
  
        self.players = manager.list( [Player(PLAYER_ONE), Player(PLAYER_TWO), PLAYER(PLAYER_THREE) ]
        self.car1 = manager.list( [Car1(i) for i in range(2)] )
        self.car2 = manager.list( [Car2(i) for i in range(2)] )
        self.car3 = manager.list( [Car3(i) for i in range(2)] )
        self.running = True
        self.lock = Lock()
  
    def get_player(self,side):
        return self.players[side]

    def get_car1(self):
        for i in range(2):
        return self.car1[i]
    
    def get_car2(self):
        for i in range(2):
        return self.car2[i]
  
    def get_car3(self):
        for i in range(2):
        return self.car3[i]
  
    def is_running(self):
        return self.running

    def stop(self):
        pos1 = self.players[0].pos[1]
        pos2 = self.players[1].pos[1]
        pos3 = self.players[2].pos[1]
        if pos1 <= 0:
            self.winner = 1 #guardamos el ganador por si lo queremos poner luego por pantalla
            self.running.value = 0
        if pos2 <= 0:
            self.winner = 2
            self.running.value = 0
        if pos3 <= 0:
            self.winner = 3
            self.running.value = 0

  def moveUp(self,player):
      self.lock.acquire()
      p = self.players[player]
      p.moveUp()
      self.players[player] = p
      self.lock.release()

   def moveDown(self,player):
      self.lock.acquire()
      p = self.players[player]
      p.moveDown()
      self.players[player] = p
      self.lock.release() 
    
  def player_collide(self,player): #Para cuando algún conejo se choque con un coche
      self.lock.acquire()
      p=self.players[player]
      p.reiniciar_P()
      self.players[player]=p
      seelf.lock.release()
       
  def get_into(self):
  #Diccionario que nos de las posiciones de todos los elementos en pantalla
      pos_Car1=[]
      for i in range (2):
          pos_Car1.append(self.car1[i].get_pos())
      pos_Car2=[]
      for i in range (2):
          pos_Car2.append(self.car2[i].get_pos())
      pos_Car3=[]
      for i in range (2):
          pos_Car3.append(self.car3[i].get_pos())
      info={'pos_player_one':self.player[PLAYER_ONE].get_pos(),
          'pos_player_two':self.player[PLAYER_TWO].get_pos(),
          'pos_player_three':self.player[PLAYER_THREE].get_pos(),
          'pos_car_one':pos_Car1,'pos_car_two':pos_Car2,'pos_car_three':pos_Car3,
         'is_running':self.running.value==1}
      return info
  
  def move_car1(self):
      self.lock.acquire()
      for i in range(2):
      coche1=self.car1[i]
      coche1.update()
      pos=coche1.get_pos()
      if pos[0]>=WIDTH:
          coche1=Car1(i)
      self.car1[i]=coche1
      self.lock.release()
    
  def move_car2(self):
      self.lock.acquire()
      for i in range(2):
      coche2=self.car2[i]
      coche2.update()
      pos=coche2.get_pos()
      if pos[0]>=WIDTH:
          coche2=Car2(i)
      self.car2[i]=coche2
      self.lock.release()

  def move_car3(self):
      self.lock.acquire()
      for i in range(2):
      coche3=self.car3[i]
      coche3.update()
      pos=coche3.get_pos()
      if pos[0]>=WIDTH:
          coche3=Car3(i)
      self.car3[i]=coche3
      self.lock.release()


  
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
                elif command=="collide": #para cuando algún conejo  se choque con algún coche
                    game.player_collide(side)
        
          
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

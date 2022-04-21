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

HEIGHT=800
WIDTH=800
PLAYER_ONE=0
PLAYER_TWO=1
PLAYER_THREE=2
MOVEMENT=20
SIDESSTR = ["left", "centre","right"]
X = 0
Y = 1


class Player():
#clase de los conejos, para indicar su tamaÃ±o, su posiciÃ³n y sus movimientos
    def __init__(self,side):
        self.side = side
        if side == PLAYER_ONE:
            self.pos = [WIDTH/4,HEIGHT-30]
        if side == PLAYER_TWO:
            self.pos=[WIDTH/2,HEIGHT-30]
        if side == PLAYER_THREE:
            self.pos = [3*WIDTH/4,HEIGHT-30]
  
    def get_pos(self):
        return self.pos
  
    def get_side(self):
        return self.side
 
    def moveDown(self):
        self.pos[1] += MOVEMENT
        if self.pos[1] > HEIGHT-30:
            self.pos[1] = HEIGHT-30
  
    def moveUP(self):
        self.pos[1] -= MOVEMENT
  
    def reiniciar_P(self):
        self.pos[1] = HEIGHT-30
      
    def __str__(self):
        return f"P<{SIDESSTR[self.side]},{self.pos}>"
      


class Car():
    #Clase de los coches.    
    def __init__(self,n):
        l = [100,300,500]
        self.index = n         
        self.y = l[self.index]
        if self.index == 0:
            self.x = rd.randint(-1000,-1)             
            self.pos = [self.x , self.y]
            self.vel = 6
        if self.index == 2:
            self.x = rd.randint(-1000,-1)             
            self.pos = [self.x , self.y]
            self.vel = 3
        if self.index == 1:
            self.x = rd.randint(-1000,-1)            
            self.pos = [self.x , self.y]
            self.vel = 4
    
    def get_pos(self):
        return self.pos         
        
    def update(self):        
        
        self.pos[Y] = self.pos[Y] 
        self.pos[X] += self.vel 
     
    def __str__(self):
        return f"B<{self.pos}>"  

  
  

  
class Game(): 
  
    def __init__(self, manager):
  
        self.players=manager.list([Player(PLAYER_ONE), Player(PLAYER_TWO), Player(PLAYER_THREE)])
        self.cars=manager.list([Car(i) for i in range(3)])
        self.running=Value('i', 1) # 1 running
        self.lock=Lock()
  
    def get_player(self,side):
        return self.players[side]

    def get_car(self):
        for i in range(3):
            return self.cars[i]
  
    def is_running(self):
        return self.running.value == 1

    def stop(self):
        pos1 = self.players[0].pos[1]
        pos2 = self.players[1].pos[1]
        pos3 = self.players[2].pos[1]
        if pos1 <= 0:
            self.running.value = 0
        if pos2 <= 0:
            self.running.value = 0
        if pos3 <= 0:
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
    
    def first_collide(self, player): #Para cuando el primer conejo se choque con un coche
        
        self.lock.acquire()
        p = self.players[PLAYER_ONE]
        p.reiniciar_P()
        self.players[PLAYER_ONE] = p
        self.lock.release()
        
    def second_collide(self, player): #Para cuando el segundo conejo se choque con un coche
        
        self.lock.acquire()
        p = self.players[PLAYER_TWO]
        p.reiniciar_P()
        self.players[PLAYER_TWO] = p
        self.lock.release()
        
    def third_collide(self, player): #Para cuando el tercer conejo se choque con un coche
        
        self.lock.acquire()
        p = self.players[PLAYER_THREE]
        p.reiniciar_P()
        self.players[PLAYER_THREE] = p
        self.lock.release()
          
    def get_info(self):
    #Diccionario que nos de las posiciones de todos los elementos en pantalla
        pos_Car=[]
        for i in range (3):
            pos_Car.append(self.cars[i].get_pos())

        info={'pos_player_one':self.players[PLAYER_ONE].get_pos(),
          'pos_player_two':self.players[PLAYER_TWO].get_pos(),
          'pos_player_three':self.players[PLAYER_THREE].get_pos(),
          'pos_cars': pos_Car,
         'is_running':self.running.value == 1
         }
        return info

    def move_car(self):
        self.lock.acquire()
        for i in range(3):
            coche=self.cars[i]
            coche.update()
            pos=coche.get_pos()
            if pos[0]>=WIDTH:
                coche=Car(i)
            self.cars[i]=coche
        self.lock.release()

    def __str__(self):     
        return f"G<{self.players[PLAYER_ONE]}:{self.players[PLAYER_TWO]}:{self.players[PLAYER_THREE]}{self.running}"

def player(side,conn,game):
    try:
        print(f"starting player {SIDESSTR[side]}:{game.get_info()}")
        conn.send((side,game.get_info()))
        while game.is_running():
            command=""
            while command != "next":
                command=conn.recv()
                if command=="up": #para que la tecla "up" haga que avance el conejo
                    game.moveUp(side)
                elif command=="down": #para que la tecla "down" haga que retroceda el conejo
                    game.moveDown(side)
                elif command == "quit": #para terminar el juego pulsando escape
                    game.finish()          
                elif command == "firstcollide" and side == 0:
                    game.first_collide(side)
                elif command == "secondcollide" and side == 1:
                    game.second_collide(side)
                elif command == "thirdcollide" and side == 2:
                    game.third_collide(side)
        
        if side == 1 or side == 2:
                game.move_car()
                if game.stop():
                    return f"GAME OVER"
        conn.send(game.get_info())
                  
    except:
        traceback.print_exc()
        conn.close()
    
    finally:
        print(f"Game ended {game}")
    

def main(ip_address):
    manager = Manager()
    try:
        with Listener((ip_address, 6000),
                      authkey=b'secret password') as listener:
            n_player = 0
            players = [None, None,None]
            game = Game(manager)
            while True:
                print(f"accepting connection {n_player}")
                conn = listener.accept()
                players[n_player] = Process(target=player,
                                            args=(n_player, conn, game))
                n_player += 1
                if n_player == 3:
                    players[0].start()
                    players[1].start()
                    players[2].start()
                    n_player = 0
                    players = [None,None,None]
                    game = Game(manager)

    except Exception as e:
        traceback.print_exc()
                    

  
if __name__=='__main__':
    ip_address="127.0.0.1"
    if len(sys.argv)>1:
        ip_address=sys.argv[1]
    main(ip_address)



from multiprocessing.connection import Listener
from multiprocessing import Process, Manager, Value, Lock
import traceback
import sys

HEIGHT=400
WIDTH=600
PLAYER_ONE=0
PLAYER_TWO=1
PLAYER_THREE=2
POS_INI = [(100,20),(300,20),(500,20)]
MOVEMENT=20

class Player():
  def __init__(self,side):
    self.side=side
    if side==PLAYER_ONE
      self.pos=[WIDHT/4,0]
    if side==PLAYER_TWO
      self.pos=[WIDTH/2,0]
    if side==PLAYER_THREE
      self.pos=[3*WIDTH/4,0]
  
  def get_pos(self):
    return self.pos
  
  def get_side(self):
    return self.side
 
  def moveDown(self):
    self.pos[Y]+=MOVEMENT
    if self.pos[Y]>HEIGHT:
      self.pos[Y]=HEIGHT
  
  def moveUP(self):
    self.pos[Y]+=MOVEMENT
    if self.pos[Y]<0:
      self.pos[Y]=0
      
  def __str__(self):
    return f"P<{SIDESSTR[self.side]},{self.pos}>"
      
  
class Car1():
  
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
  
  
if __name__=='__main__':
  
  
         

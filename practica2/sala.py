from multiprocessing.connection import Listener
from multiprocessing import Process, Manager, Value, Lock
import traceback
import sys

HEIGHT=400
WIDTH=600
PLAYER_ONE=0
PLAYER_TWO=1
PLAYER_THREE=2
FPS=30

class Player():
  
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
  
  
         

import multiprocessing.connection import client
import traceback
import pygame
import sys, os

HEIGHT=400
WIDTH=600

PLAYER_ONE=0
PLAYER_TWO=1
PLAYER_THREE=2

SIDES=["left","right"]
SIDESSTR=["left","rigth"]

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
  
class Car1():
  
class Car2():
  
class Car3():
  
  
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

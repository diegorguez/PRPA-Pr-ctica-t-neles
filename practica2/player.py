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
    

  

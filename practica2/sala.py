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

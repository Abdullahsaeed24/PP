#import needed tools
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import math
import os
import glob
import shutil
import time
import pygame




CarData = {"Time":[],
           "E":[],
           "N":[],
           "HeadingAngle":[],
           "Velocity":[]}


def calculate_tan(deg):
    radians = (math.pi / 180) * deg

    return math.tan(radians)


def VUT_Speed(x,y) -> None:

    ''' ploting the vehicle speed over time
    INPUT: None

    OUTPUT:None
    '''
    plt.subplot(1,1,1)
    plt.plot(x,y,marker = 'o',mec = 'r')
    plt.xlabel("mx",color ="c" , size = 15)
    plt.ylabel("y",color ="c" , size = 15)
    plt.grid()
    plt.show()

y = list(range(0,10 ,1))
x = list(range(0,10 ,1))
mx = []

headingAngle = calculate_tan(30)
print(headingAngle)
for i in x:
    mx.append(i*headingAngle)
print(mx)


TRACK =pygame.image.load("track.png")
RED_CAR = pygame.image.load("redcar.png")

TrackWidth , TrackHeight = TRACK.get_width() , TRACK.get_height()
WIN = pygame.display.set_mode((TrackWidth,TrackHeight))
pygame.display.set_caption("VUT ROAD")




"""
the slope equations

m = (y2-y1)/(x2-x1)


"""

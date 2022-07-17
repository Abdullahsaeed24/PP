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


headingAngle = 30
b = 0
def calculate_tan(deg):
    radians = (math.pi / 180) * deg

    return math.tan(radians)


def Start(E_0 : float , N_0 : float , HeadingAngle : int):
    global CarData

    CarData["E"].append(E_0)
    CarData["N"].append(E_0)
    CarData["Time"].append(0)
    CarData["HeadingAngle"].append(HeadingAngle)
    CarData["Velocity"].append(0)


def accelerate(speed :"m/s" , time :"second"):

    s = speed/1000
    t = time*1000
    print(s,t)
    global headingAngle
    m = calculate_tan(headingAngle)
    global b


    for i in range(0,t+50,50):

        CarData["E"].append(s*i)
        CarData["N"].append(s*m + b)
        CarData["Time"].append(i)
        CarData["HeadingAngle"].append(headingAngle)
        CarData["Velocity"].append(s*i)




def drive(time,lasts,lastt):

    t = time *1000 +3000
    s = 150
    ss=50/1000
    m = calculate_tan(30)
    for i in range(3050,t+50,50):

        CarData["E"].append((s+ss)*i)
        CarData["N"].append((s+ss)*m )
        CarData["Time"].append(i+3050)
        CarData["HeadingAngle"].append(headingAngle)
        CarData["Velocity"].append((s+ss)*i)




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




Start(0,0,45)
accelerate(50,3)
drive(10,150,3000)
#VUT_Speed(CarData["Time"],CarData["Velocity"])

d = pd.DataFrame(CarData)
print(d)

#TRACK =pygame.image.load("track.png")
#RED_CAR = pygame.image.load("redcar.png")

#TrackWidth , TrackHeight = TRACK.get_width() , TRACK.get_height()
#WIN = pygame.display.set_mode((TrackWidth,TrackHeight))
#pygame.display.set_caption("VUT ROAD")



"""
the slope equations

m = (y2-y1)/(x2-x1)


"""

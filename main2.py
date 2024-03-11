from classes import *
from graphics import *
import random
import math
from time import sleep

#sets up dimentions for the window.
frameWidth, frameHeight=1200    , 1000

#sets up the pace for everything
pace = 0.01

win = GraphWin("moving circle", frameWidth , frameHeight)
win.setBackground('lightblue')

def getRandomRGB(minR,maxR,minG,maxG,minB,maxB):
  r = random.randint(minR,maxR)
  g = random.randint(minG,maxG)
  b = random.randint(minB,maxB)
  color = color_rgb(r, g, b)
  return color

def setupBludgers(count):
  bl = [] #list of bludger objects
  for i in range(count):
    weight = random.randint(3,25)
    radius = 5
    edgespace = 200
    x = random.randint(0+edgespace,frameWidth-edgespace)
    y = random.randint(0+edgespace,frameHeight-edgespace)
    speed = 50*pace*(random.randint(10000,12000)/10000)
    angle = random.randint(0,360)
    color = getRandomRGB(80,120,40,60,30,40)
    window = win
    g = Bludger(x,y,radius,color,speed,angle,weight,window)
    g.adjustRadius()
    bl.append(g)
  return bl

def drawBludgers(lst):
  for bludger in lst:
    bludger.draw()

def moveBludgers(lst):
  for bludger in lst:
    bludger.move()
    

def bounceBludgers(lst):
  for bludger in lst:
    r = bludger.getRadius()
    x = bludger.getX()
    y = bludger.getY()
    oldTheta = bludger.getTheta()
    newTheta = oldTheta
    #bounce off left and right:
    if x < r or x > frameWidth-r:
      newTheta = math.pi - oldTheta
    if y < r or y > frameHeight-r:
      newTheta = - newTheta
    bludger.setTheta(newTheta)

def measureDistance(point1,point2):
  xDist = point1.getX()-point2.getX()
  yDist = point1.getY()-point2.getY()
  distance = math.sqrt(xDist**2+yDist**2)
  return distance

def getVector(bPoint,pPoint):
  xDist = bPoint.getX()-pPoint.getX()
  yDist = bPoint.getY()-pPoint.getY()
  distance = measureDistance(bPoint,pPoint)
  if yDist <= 0:
    theta = math.acos(-xDist/distance)
  else:
    theta = math.pi+math.acos(xDist/distance)
  
  return theta,distance
  
def swerveBludgers(player,lst):
 
  for bludger in lst:
    point1 = bludger.getLocation()
    point2 = player.getLocation()
    theta, distance = getVector(point1, point2)
    force = bludger.getWeight() * player.getWeight()/distance**2
    bludger.adjustCourse(theta, force)
    bludger.showIndicator(theta, distance)
    
    for bludger2 in lst:
      if bludger2 != bludger:
        point2 = bludger2.getLocation()
        if measureDistance(point1, point2) > 10:
          theta, distance = getVector(point1, point2)
          force = bludger.getWeight()*bludger2.getWeight()/distance**2
          

          bludger.adjustCourse(theta, force)
          bludger.showIndicator(theta, 1000*distance)
def removeBludgers(bl):
  for i in bl:
    x = i.getX()
    y = i.getY()
    if x < 0-frameWidth or x > 2*frameWidth or y < 0-frameHeight or y >2* frameHeight:
        bl.remove(i)
      

    
def doFrame(player,bl):
  
  #bounceBludgers(bl)
  moveBludgers(bl)
  swerveBludgers(player, bl)
  #removeBludgers(bl)
  
  
  
def main():

  done = False  
  #bludgers
  bl = setupBludgers(1)

  print('bludgers created')
  drawBludgers(bl)
  print('bludgers drawn')


  #players
  pl = Player(frameWidth/2, frameHeight/2, 5, win)
  pl.draw()
  
  reps = 0
  while done == False and reps < 10**5:
    doFrame(pl,bl)
    sleep(pace/100)
    #done = checkDone()
    reps += 1
main()

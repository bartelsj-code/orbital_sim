from graphics import *
import math

class Bludger:
  #The name is wrong. This started out as a quidditch game and turned into a planetary orbit sim so it should be renamed to Body, or Planet, or something like that
  #Well, the first thing this class did badly was have near to no comments at the top
  '''
  This class is too big! It takes care of too many things at once.
  This class also carries too many responsibilities. '''

  '''Needs less instance variables. I have a really hard time undertanding though how to improve cohesion here.
  Would I use separate classes to deal with appearnce, Size, Rendering, Location, Movement, Speed, Angle, Display Coords...?
  This would allow me to have a class like PlanetMovementVector with a method like adjust_vector(self, accelerationVector) which adjusts
  the self.speed and self.angle of the PlanetMovementVector and maybe an AccelerationVector class with a method like setVector(self, force)
  I think an approach like this could vastly increase cohesion
  '''
  def __init__(self, x, y, radius, color, speed, angle, weight, win):
      self.x = x
      self.y = y
      self.weight = weight
      self.xAdjustment = 0
      self.yAdjustment = 0
      self.radius = radius
      self.color = color
      self.location = Point(x, y)
      self.speed = speed
      self.theta = (2*math.pi*angle)/360
      self.shape1 = Circle(self.location, radius)
      self.shape1.setFill(self.color)
      self.indicator = Line(Point(0,0),Point(0,0))
      self.indicator2 = Line(Point(0,0),Point(0,0))
      
      self.win = win
      
  def getWeight(self):
    return self.weight
    
  def setWeight(self, weight):
    self.weight = weight
    self.adjustRadius()
    
  def adjustRadius(self):

    self.radius = (3*self.weight/(4 * math.pi))**(1./3)
    
  def draw(self):
    self.shape1.draw(self.win)

  def setColor(self, color):

    self.color = color
    self.shape1.setFill(self.color)

  def undraw(self):
    self.shape1.undraw()

  def getX(self):
    return self.x

  def setX(self, x):
    self.x = x

  def getY(self):
    return self.y

  def setY(self, y):
    self.y = y
    
  def getRadius(self):
    return self.radius
    
  def setSpeed(self, speed):
    self.speed = speed

  def getTheta(self):
    return self.theta

  def setTheta(self, theta):
    self.theta = theta

  def updateLocation(self):
    self.location = Point(self.x,self.y)

  def getLocation(self):
    return self.location
    
  def move(self):
    dx = math.cos(self.theta)*self.speed
    dy = math.sin(self.theta)*self.speed
    self.theta = self.theta % (2 * math.pi)
    self.shape1.move(dx, dy)
    p1 = Point(self.x,self.y)
    self.setX(self.x+dx)
    self.setY(self.y+dy)
    p2 = Point(self.x,self.y)
    indicator = Line(p1,p2)
    indicator.draw(self.win)
    self.updateLocation()

  def adjustCourse(self,theta,force):
    ndx = math.cos(self.theta)*self.speed + math.cos(theta)*force
    ndy = math.sin(self.theta)*self.speed + math.sin(theta)*force

    #calculate new theta and new speed
    newSpeed = math.sqrt(ndx**2+ndy**2)
    if ndy >= 0:
      newTheta = math.acos(ndx/newSpeed)
    else:
      newTheta = math.pi+math.acos(-ndx/newSpeed)
      
    self.speed = newSpeed
    self.theta = newTheta
    p1 = self.location
    p2 = Point(self.getX()+ndx,self.getY()+ndy)
  
  def showIndicator(self,theta,length):
    dx = math.cos(theta)*length
    dy = math.sin(theta)*length
    p2 = Point(self.getX()+dx,self.getY()+dy)
    #indicator = Line(self.location,p2)
    #indicator.draw(self.win)
    
      
class Player:
  def __init__(self, x , y, weight, win):
    self.x = x
    self.y = y
    self.location = Point(self.x,self.y)
    self.indicator = Circle(self.location,weight)
    self.indicator.setFill('White')
    self.win = win
    self.weight = weight
    
  def getWeight(self):
    return self.weight

  def draw(self):
    self.indicator.draw(self.win)

  def getLocation(self):
    return self.location
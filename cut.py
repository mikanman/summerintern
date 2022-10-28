import math

class Max_Min():

  def __init__(self, size):
    self.max = 0
    self.min = size
    self.size = size

  def update(self, i):
    if i > self.max:
      self.max = int(i)

    if i < self.min:
      self.min = int(i)

class Make_Dice():

  def __init__(self, x_mize, y_mize):
    self.y_max = y_mize.max
    self.y_min = y_mize.min
    self.x_max = x_mize.max
    self.x_min = x_mize.min
    self.width = x_mize.size
    self.height = y_mize.size
    self.plus = 10


  def update(self):
    x_range = self.x_max - self.x_min
    y_range = self.y_max - self.y_min
    y_x = y_range - x_range

    if y_x >= 0:
      self.y_max += self.plus
      self.y_min -= self.plus
      self.x_max  += math.ceil(y_x/2) + self.plus
      self.x_min -= math.floor(y_x/2) + self.plus
    
    else:
      self.x_max += self.plus
      self.x_min -= self.plus
      self.y_max += math.ceil( -(y_x)/2 ) + self.plus
      self.y_min -= math.floor( -(y_x)/2 ) + self.plus


    if self.x_min < 0:
      x = -self.x_min
      self.x_min += x
      self.y_min += x

    if self.y_min < 0:
      y = -self.y_min
      self.x_min += y
      self.y_min += y

    if self.x_max < 0 :
      x = self.x_max
      self.x_min = self.width
      self.y_min -= x

    if self.y_max < 0:
      y = self.y_max
      self.x_min -= y
      self.y_min = self.height
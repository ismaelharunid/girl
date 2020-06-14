
from girl.common import *
from girl.typehelpers import *


class Area(object):
  
  @property
  def offset(self):
    raise NotImplementedError("Please implement the offset property")
  
  @property
  def size(self):
    raise NotImplementedError("Please implement the size property")
  
  @property
  def x0(self):
    raise NotImplementedError("Please implement the x0 property")
  
  @property
  def y0(self):
    raise NotImplementedError("Please implement the y0 property")
  
  @property
  def x1(self):
    raise NotImplementedError("Please implement the x1 property")
  
  @property
  def y1(self):
    raise NotImplementedError("Please implement the y1 property")
  
  def __iter__(self):
    yield self.x0
    yield self.y0
    yield self.x1
    yield self.y1
  
  def __add__(self, offset):
    if is2numtuple(offset):
      return self.__class__((self.x0+offset[0], self.y0+offset[1]
          , self.x1+offset[0], self.y1+offset[1]))
    raise ValueError("Bounds expects numeric 2-tuple but found {:s}" \
        .format(type(offset).__name__))
  
  def __sub__(self, offset):
    if is2numtuple(offset):
      return self.__class__((self.x0-offset[0], self.y0-offset[1]
          , self.x1-offset[0], self.y1-offset[1]))
    raise ValueError("Bounds expects numeric 2-tuple but found {:s}" \
        .format(type(offset).__name__))
  
  def __mul__(self, delta):
    if isinstance(delta, Number):
      delta = (delta,delta)
    if is2numtuple(delta):
      return self.__class__((self.x0*delta[0], self.y0*delta[1]
          , self.x1*delta[0], self.y1*delta[1]))
    raise ValueError("Bounds expects numeric or 2-tuple but found {:s}" \
        .format(type(delta).__name__))
  
  def __truediv__(self, delta):
    if isinstance(delta, Number):
      delta = (delta,delta)
    if is2numtuple(delta):
      return self.__class__((self.x0/delta[0], self.y0/delta[1]
          , self.x1/delta[0], self.y1/delta[1]))
    raise ValueError("Bounds expects numeric or 2-tuple but found {:s}" \
        .format(type(delta).__name__))
  
  def __floordiv__(self, delta):
    if isinstance(delta, Number):
      delta = (delta,delta)
    if is2numtuple(delta):
      return self.__class__((self.x0/delta[0], self.y0/delta[1]
          , self.x1/delta[0], self.y1/delta[1]))
    raise ValueError("Bounds expects numeric or 2-tuple but found {:s}" \
        .format(type(delta).__name__))
  
  def __divmod__(self, delta):
    if isinstance(delta, Number):
      delta = (delta,delta)
    if is2numtuple(delta):
      return self.__class__((divmod(self.x0,delta[0]), divmod(self.y0,delta[1])
          , divmod(self.x1,delta[0]), divmod(self.y1,delta[1])))
    raise ValueError("Bounds expects numeric or 2-tuple but found {:s}" \
        .format(type(delta).__name__))
  
  def __mod__(self, delta):
    if isinstance(delta, Number):
      delta = (delta,delta)
    if is2numtuple(delta):
      return self.__class__((self.x0%delta[0], self.y0%delta[1]
          , self.x1%delta[0], self.y1%delta[1]))
    raise ValueError("Bounds expects numeric or 2-tuple but found {:s}" \
        .format(type(delta).__name__))
  
  def __repr__(self):
    return "{:s}({:d}, {:d}, {:d}, {:d})" \
        .format(self.__class__.__name__, self.x0, self.y0, self.x1, self.y1)
  
  def asbounds(self):
    return Rectangle(self)
  
  def asrectangle(self):
    return Rectangle(self)



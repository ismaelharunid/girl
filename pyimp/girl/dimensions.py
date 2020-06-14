
from .common import *
from .typehelpers import *
from .interfaces import Area


class Size(object):
  
  def __init__(self, initialzer):
    if isinstance(initialzer, Iterable):
      size = tuple(int(c) for c in initialzer)
      if len(size) == 2:
        self._size = size
        return
    raise ValueError("Size expects a numeric 2-tuple but found {:s}" \
        .format(type(initialzer).__name__))
  
  def __iter__(self):
    yield self.width
    yield self.height
  
  def __repr__(self):
    return "Size({:d}, {:d})".format(self.width, self.height)


class Bounds(Area):
  
  _offset = None
  _size   = None
  
  @property
  def offset(self):
    return self._offset
  
  @property
  def size(self):
    return self._size
  
  @property
  def width(self):
    return self._size[0]
  
  @property
  def height(self):
    return self._size[1]
  
  @property
  def x0(self):
    return self._offset[0]
  
  @property
  def y0(self):
    return self._offset[1]
  
  @property
  def x1(self):
    return self._offset[0] + self.width
  
  @property
  def y1(self):
    return self._offset[1] + self.height
  
  def __init__(self, initialzer):
    if isinstance(initialzer, Iterable):
      bounds = tuple(int(c) for c in initialzer)
      if len(bounds) == 2:
        bounds = (0, 0, bounds[0], bounds[1])
      if len(bounds) == 4:
        self._offset = bounds[0:2]
        self._size = (bounds[2]-bounds[0], bounds[3]-bounds[1])
        return
    raise ValueError("Bounds expects a numeric 2 or 4-tuple but found {:s}" \
        .format(type(initialzer).__name__))


class Frame(Bounds):
  
  _parent = None
  
  def __init__(self, initializer, parent=None):
    self._parent = parent
    super().__init__(initializer)
  
  @property
  def x0(self):
    return self._offset[0] + self._parent.x0 if self._parent else self._offset[0]
  
  @property
  def y0(self):
    return self._offset[1] + self._parent.y0 if self._parent else self._offset[1]
  
  @property
  def x1(self):
    return self.x0 + self.width
  
  @property
  def y1(self):
    return self.y0 + self.height

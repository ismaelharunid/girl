
from .interfaces import Drawable, Tile


class Tileable(Drawable):
  """
  girl.Tileable class interface for that can be referenced by tile.  
  """
  
  def __new__(cls, size, tilesize, stride, bpp, cpp
      , offset=(0,0)):
    self = super(Drwable, cls).__new__(cls, size, stride, bpp, cpp)
    self._tilesize    = tilesize
    return self
  
  _tilesize = None
  


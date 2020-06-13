
from .pixelmap import PixelMap
from .writable import Writable


class Tile(Writable, PixelMap):
  """
  girl.Tile class interface.
  """
  
  def __new__(cls, image):
    self = super(Tile, cls).__new__(cls, image)
    return self
  
  _image = None       # the owner image
  
  


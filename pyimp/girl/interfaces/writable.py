

from .interfaces import PixelMap


class Writable(PixelMap):
  """
  girl.Writable Class interface for writable PixelMap.
  """
  
  def __setitem__(self, key, iteratable):
    raise NotImplementedError("Please implement the __setitem__ magic method")
  

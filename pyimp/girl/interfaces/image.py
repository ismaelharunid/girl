

from .pixelmap import PixelMap


class Image(PixelMap):
  """
  girl.Image class interface that can be loaded, and is moded and tiled.
  """
  
  _MODES     = ()
  
  @classmethod
  @property
  def MODES(cls):
    return tuple(cls._MODES)
  
  @classmethod
  def open(self):
    raise NotImplementedError("Please implement the open class method")
  
  _mode     = None
  _offset   = None
  
  def __new__(cls, size, mode, bpp, cpp, tilesize
      , offset=(0,0)):
    self = super(Image, cls).__new__(cls, size, stride, bpp, cpp)
    self._mode      = mode
    self._offset    = offset
    return self
  
  @property
  def mode(self):
    return self._mode
  
  @property
  def tilesize(self):
    return tuple(self._tilesize)
  
  @property
  def tilewidth(self):
    return self._tilesize[0]
  
  @property
  def tileheight(self):
    return self._tilesize[1]
  
  @property
  def columns(self):
    return self._size[0] / self._tilesize[0]
  
  @property
  def rows(self):
    return self._size[1] / self._tilesize[1]
  
  @property
  def tiles(self):
    raise NotImplementedError("Please implement the tiles property")
  
  def close(self):
    raise NotImplementedError("Please implement the close method")
  
  def flush(self):
    raise NotImplementedError("Please implement the flush method")
  
  def save(self):
    raise NotImplementedError("Please implement the save method")
  
  def write(self):
    raise NotImplementedError("Please implement the write method")
  

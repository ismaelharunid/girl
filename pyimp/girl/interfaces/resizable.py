

from .interfaces import PixelMap


class Resizable(PixelMap):
  """
  girl.Resizable Class interface for a resizable PixelMap.
  """
  
  def resize(self, newsize=None, newbpp=None, newcpp=None
      , offset=(0,0), startbpp=0, startcpp=0)):
    """
    resize the bitmap.
    
    newsize(2tuple[width, height]): the size of the new bitmap
    newbpp(int):              the bpp for the new bitmap
    newcpp(int):              the cpp for the new bitmap
    offset(2tuple[int, int]:  starting pixel[rank, file]
    startbpp(int):            starting byte
    startcpp(int):            starting channel
    """
    raise NotImplementedError("Please implement the resize method")
  

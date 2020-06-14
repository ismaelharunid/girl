


class PixelMap(object):
  """
  girl.PixelMap class interface.
  """
  
  _bpc            = None    # bytes per channel
  _cpp            = None    # channels per pixel
  _size           = None    # 2-tuple (pixel width and height)
  _columnstride   = None    # number of bytes to the next column
  _rowstride      = None    # number of bytes to the next row
  _channelstride  = None    # number of bytes to the next channel
  
  def __init__(self, size, cpp, bpc
      , columnstride, rowstride, channelstride):
    print('PixelMap#__init__')
    self._size          = size
    self._cpp           = cpp
    self._bpc           = bpc
    self._columnstride  = columnstride
    self._rowstride     = rowstride
    self._channelstride = channelstride

  @property
  def columnstride(self):
    return self._columnstride
  
  @property
  def rowstride(self):
    return self._rowstride
  
  @property
  def channelstride(self):
    return self._channelstride
  
  @property
  def bpc(self):
    return self._bpc
  
  @property
  def bpp(self):
    return self._bpc * self._cpp
  
  @property
  def cpp(self):
    return self._cpp
  
  @property
  def data(self):
    raise NotImplementedError("Please implement the data property")
  
  @property
  def height(self):
    return self._size[1]
  
  @property
  def size(self):
    return tuple(self._size)
  
  @property
  def width(self):
    return self._size[0]
  
  def __getitem__(self, key):
    raise NotImplementedError("Please implement the __getitem__ magic method")
  
  def tostring(self):
    raise NotImplementedError("Please implement the tostring method")
  
  def toarray(self):
    raise NotImplementedError("Please implement the toarray method")
  
  def totuple(self):
    raise NotImplementedError("Please implement the totuple method")
  
  def toflattuple(self):
    raise NotImplementedError("Please implement the toflattuple method")
  

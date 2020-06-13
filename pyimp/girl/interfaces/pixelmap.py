


class PixelMap(object):
  """
  girl.PixelMap class interface.
  """
  
  _bpp            = None    # bytes per pixel
  _cpp            = None    # channels per pixel
  _size           = None    # 2-tuple (pixel width and height)
  _columnstride   = None    # number of bytes to the next column
  _rowstride      = None    # number of bytes to the next row
  _pixelstride    = None    # number of bytes to the next pixel
  _channelstride  = None    # number of bytes to the next channel
  
  def __new__(cls, size, bpp, cpp, columnstride, rowstride
      , pixelstride, channelstride):
    self = super(Image, cls).__new__(cls)
    self._size          = size
    self._bpp           = bpp
    self._cpp           = channels
    self._columnstride  = columnstride
    self._rowstride     = rowstride
    self._pixelstride   = pixelstride
    self._channelstride = channelstride
    return self
  
  @property
  def bpp(self):
    return self._bpp
  
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
  

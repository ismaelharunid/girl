

from girl.interfaces import PixelMap
from girl.common import *
from girl.typehelpers import *
from girl.interfaces import Area

class RawPixelMap(PixelMap, bytearray):
  
  _dtype = 'uint8'
  
  def __new__(cls, size, cpp, bpc):
    dlength = size[0] * size[1] * cpp * bpc
    self = bytearray.__new__(cls, dlength, 'ascii')
    print('RawPixelMap.__new__', dlength, bytearray.__len__(self))
    self._dlength = dlength
    return self
  
  _dlength  = None
  _data     = None
  
  @property
  def dlength(self):
    return self._dlength
  
  def __init__(self, size, cpp, bpc):
    print('RawPixelMap#__init__')
    bytearray.__init__(self, self._dlength)
    channelstride = bpc
    columnstride  = bpc * cpp
    rowstride     = bpc * cpp * size[0]
    super().__init__(size, cpp, bpc, columnstride, rowstride, channelstride)
  
  def __key__(self, key):
    t_key = type(key)
    #print("__key__", key, t_key.__name__)
    if t_key in (int, slice):
      key = (key,)
    if t_key is tuple:
      # columns
      key3 = slice(0,None,1)
      key2 = slice(0,None,1)
      key1 = slice(0,None,1)
      key0 = slice(key[0], key[0]+1, 1) if type(key[0]) is int else \
          slice(0,None,1) if key[0] is Ellipsis else \
          slice(None,None,1) if key[0] is None else \
          key[0]
      if len(key) >= 2:
        # rows
        key1 = slice(key[1], key[1]+1, 1) if type(key[1]) is int else \
            slice(0,None,1) if key[1] is Ellipsis else \
            slice(None,None,1) if key[1] is None else \
            key[1]
        if len(key) >= 3:
          # channels
          key2 = slice(key[2], key[2]+1, 1) if type(key[2]) is int else \
              slice(0,None,1) if key[2] is Ellipsis else \
              slice(None,None,1) if key[2] is None else \
              key[2]
          if len(key) >= 4:
            # bytes
            key3 = slice(key[3], key[3]+1, 1) if type(key[3]) is int else \
                slice(0,None,1) if key[3] is Ellipsis else \
                slice(None,None,1) if key[3] is None else \
                key[2]
      return (key1, key0, key2, key3)
  
  def __getitem__(self, key):
    #print("__getitem__", key)
    indexes = self.__key__(key)
    if indexes:
      rs, fs, cs = self.columnstride, self.channelstride, self.bpc
      rows, columns, channels, bytes_ = indexes
      return bytearray(self[rs*r+fs*f+cs*c+b] \
          for r in range(*rows.indices(self.height)) \
          for c in range(*columns.indices(self.width)) \
          for f in range(*channels.indices(self.cpp)) \
          for b in range(*bytes_.indices(self.bpc)))
    return bytearray.__getitem__(self, key)
  
  def __setitem__(self, key, value):
    #print("__setitem__", key)
    indexes = self.__key__(key)
    if indexes:
      rs, fs, cs = self.columnstride, self.channelstride, self.bpc
      rows, columns, channels, bytes_ = indexes
      it = iter(value)
      for r in range(*rows.indices(self.height)):
        for c in range(*columns.indices(self.width)):
          for f in range(*channels.indices(self.cpp)):
            for b in range(*bytes_.indices(self.bpc)):
              bytearray.__setitem__(self, rs*r+fs*f+cs*c+b, it.__next__())
    else:
      bytearray.__setitem__(self, key, value)

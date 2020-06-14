
from collections.abc import Iterable, Iterator, Sequence, Sized
from dataclasses import dataclass, astuple
from numbers import Number

is2tuple = lambda t: isinstance(t, tuple) and len(t) == 2

is2numtuple = lambda t: isinstance(t, tuple) and len(t) == 2 \
    and all(isinstance(i, Number) for i in t)

isntuple = lambda t,n,c=None: isinstance(t, tuple) and len(t) == n \
    and (c is None or all(isinstance(i, c) for i in t))

def zrange(count, z=0):
  while count > 0:
    count -= 1
    yield z

MAXDATAREPRSIZE = 80*5
def reprdata(data, maxitems=MAXDATAREPRSIZE, rowsize=6, n_columns=None
    , itemrepr=repr, linesize=None):
  l_data = len(data)
  n = 1 if n_columns is None else n_columns
  if l_data > maxitems:
    hmi = min(l_data, maxitems) // 2
    i1, frag = divmod(hmi, rowsize)
    i1 = i1 * rowsize + max(frag, rowsize // 2) - 1
    i2 = l_data - (maxitems-i1) + 2
    i3 = (i2 // rowsize + 1) * rowsize
    #print(l_data, i1, i2, i3)
    #('' if i%n or not i else ' ')
    out = '\n      '.join(','.join(('' if i%n or not i else ' ')+itemrepr(data[i]) \
        for i in range(j,min(i1,j+rowsize),1)) \
        for j in range(0,i1,rowsize)) + ', ...... \n......'
    #out += ','.join(itemrepr(i) for i in data[i2:i3]) + '\n      '
    out += '\n      '.join(','.join(('' if i%n or not i else ' ')+itemrepr(data[i]) \
        for i in range(j,min(l_data,j+rowsize),1)) \
        for j in range(i2,l_data,rowsize))
  else:
    out = ', '.join(itemrepr(i) for i in data)
  return '[' + out + ']'



import operator

def create_unary_op(name, op):
  def unary(a):
    rtype = type(a)
    return rtype(op(ai) for ai in a)
  unary.__name__ = name
  return unary

def create_binary_op(name, op):
  def binary(a, b):
    if isinstance(a, Sequence):
      rtype = type(a) 
      if not isinstance(b, Sequence):
        b = (b,)
    else:
      rtype = type(b)
      a = rtype((a,))
    la, lb = len(a), len(b)
    return rtype(op(a[i%la], b[i%lb]) for i in range(max(la, lb)))
  binary.__name__ = name
  return binary

SEQUENCEMATHOPS = dict((name \
    , (create_unary_op,create_binary_op)[op.__text_signature__.count(',')-2] \
    (name, op)) for (name, op) in vars(operator).items() \
    if name.startswith('__') and name.endswith('__') \
    and hasattr(operator, name.strip('_')) \
    and not name.endswith('item__'))

SEQUENCEMATHOPS.pop('__matmul__')
SEQUENCEMATHOPS.pop('__imatmul__')

SequenceMathOps = type('SequenceMathOps', (Sequence,), SEQUENCEMATHOPS)

from array import array as Array
D2ATYPES = \
    { float:    'f'
    , int:      'l'
    , str:      'B'
    , "char":   'b'
    , "uchar":  'B'
    , "int":    'l'
    , "uint":   'L'
    , "float":  'f'
    , "double": 'd'
    , "int8":   'b'
    , "uint8":  'B'
    , "int16":  'h'
    , "uint16": 'H'
    , "int32":  'l'
    , "uint32": 'L'
    , "int64":  'q'
    , "uint64": 'Q'
    }

class TypedList(Array, Sequence):
  
  _dtype    = None
  _dlength  = None
  
  @property
  def dtype(self):
    return self._dtype
  
  @property
  def dlength(self):
    return self._dlength
  
  def __new__(cls, initializer, dtype=None):
    values, dlength = initializer, None
    if dtype is None:
      dtype = cls._dtype
    if dtype is None:
      if isinstance(initializer, Iterable):
        values = tuple(initializer)
        if len(values):
          dtype = type(values[0])
    if dtype is None:
      raise ValueError("data type not specified nor can it be inferred")
    if dtype not in D2ATYPES:
      raise ValueError("unsupported data type {:s}".format(dtype.__name__))
    if isinstance(initializer, Number):
      dlength = initializer
      self = super().__new__(cls, D2ATYPES[dtype], zrange(dlength))
    else:
      self = super().__new__(cls, D2ATYPES[dtype], values)
    self._dtype = dtype
    self._dlength = dlength
    return self
  
  def __repr__(self):
    data = reprdata(self)
    return "{:s}({:s}, dtype={:s})".format \
        ( self.__class__.__name__, data, self._dtype.__name__)


def createPretypedList(name, dtype, bases=(), *amixins, **kwmixins):
  if dtype not in D2ATYPES:
    raise ValueError("unsupported item type {:s}".format(dtype.__name__))
  mixins = {}
  for mixin in amixins:
    mixins.update(mixin)
  for (method_name, method) in kwmixins.items():
    mixins[method_name] = method
  mixins["_dtype"] = dtype
  cls = type(name, (TypedList,) + tuple(bases), mixins)
  cls._dtype = dtype
  return cls




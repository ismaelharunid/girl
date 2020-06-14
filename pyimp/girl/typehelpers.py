
from collections.abc import Iterable, Iterator, Sequence, Sized
from dataclasses import dataclass, astuple
from numbers import Number

is2tuple = lambda t: isinstance(t, tuple) and len(t) == 2

is2numtuple = lambda t: isinstance(t, tuple) and len(t) == 2 \
    and all(isinstance(i, Number) for i in t)

isntuple = lambda t,n,c=None: isinstance(t, tuple) and len(t) == n \
    and (c is None or all(isinstance(i, c) for i in t))


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
    { float:  'f'
    , int:    'l'
    }

class TypedList(Array, Sequence):
  
  _dtype  = None
  
  @property
  def dtype(self):
    return self._dtype
  
  def __new__(cls, initializer, dtype=None):
    values = initializer
    if dtype is None:
      if cls._dtype is None:
        values = tuple(initializer)
        dtype = type(values[0])
      else:
        dtype = cls._dtype
    if dtype not in D2ATYPES:
      raise ValueError("unsupported item type {:s}".format(dtype.__name__))
    self = super().__new__(cls, D2ATYPES[dtype], values)
    self._dtype = dtype
    return self
  
  def __repr__(self):
    return "{:s}([{:s}], dtype={:s})".format \
        ( self.__class__.__name__
        , ', '.join(repr(c) for c in self)
        , self._dtype.__name__)


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




from collections.abc import Iterable, Iterator, Sequence, Sized
from dataclasses import dataclass, astuple
from numbers import Number


is2tuple = lambda t: isinstance(t, tuple) and len(t) == 2

is2numtuple = lambda t: isinstance(t, tuple) and len(t) == 2 \
    and all(isinstance(i, Number) for i in t)

isntuple = lambda t,n,c=None: isinstance(t, tuple) and len(t) == n \
    and (c is None or all(isinstance(i, c) for i in t))


class TypedList(list):
  pass

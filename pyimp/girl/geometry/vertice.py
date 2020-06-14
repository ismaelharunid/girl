
from girl.common import *
from girl.typehelpers import *
from math import sqrt

class Vertice(TypedList):
  
  def __new__(cls, initializer, n_columns=2):
    self = super().__new__(cls, initializer)
    self.n_columns = n_columns
    return self
  
  _dtype = float
  n_columns = 2
  
  @property
  def n_rows(self):
    return len(self) // self.n_columns

  def __repr__(self):
    n = self.n_columns
    return "{:s}([{:s}], n_columns={:d}, dtype={:s})".format \
        ( self.__class__.__name__
        , ','.join(('' if i%n or not i else ' ')+repr(self[i]) \
        for i in range(len(self))) \
        , self.n_columns, self._dtype.__name__)
  
  def transpose(self):
    return self.__class__((self[j+i*self.n_columns] \
        for j in range(self.n_columns) \
        for i in range(self.n_rows)), n_columns=self.n_rows)

  def matmul(self, mat):
    ca, ra = self.n_columns, self.n_rows
    cb = mat.n_columns if hasattr(mat, 'n_columns') else \
        int(round(sqrt(len(mat))))
    rb = len(mat) / cb
    return self.__class__((sum(self[i+k*ca]*mat[j+i*cb] for i in range(ca)) \
        for k in range(ra) for j in range(cb)), n_columns=cb)

Vertice.__matmul__ = Vertice.matmul
Vertice.__imatmul__ = Vertice.matmul
#  lambda ra,ca,a, rb,cb,b: \
#    (cb, ra, tuple(sum(a[i+k*ca]*b[j+i*cb] for i in range(ca)) \
#    for k in range(ra) for j in range(cb)))


Vertice = type('Vertice', (Vertice,), SEQUENCEMATHOPS)


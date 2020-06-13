
from .interfaces import Tileable


class Renderable(Tileable):
  """
  girl.Renderable class interface for that can be rendered to a drawable.  
  """
  
  def render(self):
    raise NotImplementedError("Please implement the render magic method")
  
  def render_to(self, bitmap):
    """
    Render to bitmap.
    
    bitmap(BitMap):   that target bitmap to render to, it must be compatible.
    raise NotImplementedError("Please implement the render_to magic method")


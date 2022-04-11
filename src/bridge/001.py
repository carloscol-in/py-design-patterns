"""
Escape complexity explosion as you get more combinations of classes.
"""

from abc import ABC


class Renderer(ABC):
    def rendering_circle(self, radius):
        pass

class VectorRenderer(Renderer):
    def rendering_circle(self, radius):
        print(f'Rendering circle of radius, using Vector renderer: {radius}')

class RasterRenderer(Renderer):
    def rendering_circle(self, radius):
        print(f'Rendering circle of radius, using Raster renderer: {radius}')

class Shape(ABC):
    def __init__(self, renderer: Renderer):
        self.renderer = renderer
        
    def draw(self): pass
    def resize(self, factor): pass

class Circle(Shape):
    def __init__(self, renderer: Renderer, radius: int):
        super().__init__(renderer)
        self.radius = radius

    def draw(self):
        self.renderer.rendering_circle(self.radius)

    def resize(self, factor):
        self.radius *= factor

if __name__ == '__main__':
    raster = RasterRenderer()
    vector = VectorRenderer()
    circle = Circle(raster, 5)
    circle.draw()
    circle.resize(2)
    circle.draw()
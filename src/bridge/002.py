from abc import ABC


class Renderer(ABC):
    @property
    def what_to_render_as(self):
        return None

# TODO: reimplement Shape, Square, Triangle and Renderer/VectorRenderer/RasterRenderer


class RasterRenderer(Renderer):
    @property
    def what_to_render_as(self):
        return f'{self.shape} as pixels'


class VectorRenderer(Renderer):
    @property
    def what_to_render_as(self):
        return f'{self.shape} as lines'


class Shape(ABC):
    def __init__(self, renderer: Renderer):
        self.renderer = renderer

    def __str__(self):
        return f'Drawing {self.renderer.what_to_render_as}'

class Square(Shape):
    def __init__(self, renderer: Renderer):
        super().__init__(renderer)
        self.renderer.shape = 'Square'


class Triangle(Shape):
    def __init__(self, renderer: Renderer):
        super().__init__(renderer)
        self.renderer.shape = 'Triangle'

if __name__ == '__main__':
    raster = RasterRenderer()
    vector = VectorRenderer()
    square = Square(raster)
    triangle = Triangle(vector)

    print(str(Triangle(RasterRenderer())))
    print(triangle)

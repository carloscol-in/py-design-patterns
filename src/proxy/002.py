class Bitmap:
    def __init__(self, filename):
        self.filename = filename
        # We shouldn't be loading the image if we're not going to draw it.
        print(f'Loading image from {self.filename}')

    def draw(self):
        print(f'Drawing image {self.filename}')

class LazyBitmap:
    """This proxy is used to avoid loading the Bitmap until it is going to be required for drawing.

    Since bitmap/image loading might be an expensive operation, you might want to delay it or use it only when it is necessary.

    Also, if you try creating a Bitmap again, the loading won't happen again, since LazyBitmap already has a Bitmap object created.
    """
    def __init__(self, filename):
        self.filename = filename
        self._bitmap = None

    def draw(self):
        if not self._bitmap:
            self._bitmap = Bitmap(self.filename)

        self._bitmap.draw()

def draw_image(image):
    print('About to draw image')
    image.draw()
    print('Done drawing the image')

if __name__ == '__main__':
    bmp = LazyBitmap('facepalm.jpg')
    draw_image(bmp)
    draw_image(bmp)
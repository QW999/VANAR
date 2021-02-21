

# https://auth0.com/blog/image-processing-in-python-with-pillow/

# image = Image.open('demo_image.jpg')
# logo = Image.open('logo.png')
# image_copy = image.copy()
# position = ((image_copy.width - logo.width), (image_copy.height - logo.height))
# image_copy.paste(logo, position)
# image_copy.save('pasted_image.jpg')

# image = Image.open('demo_image.jpg')
#
# image_rot_90 = image.rotate(90)
# image_rot_90.save('image_rot_90.jpg')
#
# image_rot_180 = image.rotate(180)
# image_rot_180.save('image_rot_180.jpg')

# image.rotate(18, expand=True).save('image_rot_18.jpg')



# image = Image.open('demo_image.jpg')
#
# image_flip = image.transpose(Image.FLIP_LEFT_RIGHT)
# image_flip.save('image_flip.jpg')


# from PIL import Image, ImageDraw
#
# canvas = Image.new('RGB', (400, 300), 'white')
# img_draw = ImageDraw.Draw(canvas)
# img_draw.rectangle((70, 50, 270, 200), outline='red', fill='blue')
# img_draw.text((70, 250), 'Hello World', fill='green')
# canvas.save('drawn_image.jpg')


# image = Image.open('demo_image.jpg')
#
# greyscale_image = image.convert('L')
# greyscale_image.save('greyscale_image.jpg')
#
# print(image.mode) # Output: RGB
# print(greyscale_image.mode) # Output: L



# image = Image.open('demo_image.jpg')
#
# red, green, blue = image.split()
#
# print(image.mode) # Output: RGB
# print(red.mode) # Output: L
# print(green.mode) # Output: L
# print(blue.mode) # Output: L
#
# new_image = Image.merge("RGB", (green, red, blue))
# new_image.save('new_image.jpg')
#
# print(new_image.mode) # Output: RGB


# from PIL import Image, ImageEnhance
#
# image = Image.open('demo_image.jpg')
#
# contrast = ImageEnhance.Contrast(image)
# contrast.enhance(1.5).save('contrast.jpg')


# color = ImageEnhance.Color(image)
# color.enhance(1.5).save('color.jpg')


# brightness = ImageEnhance.Brightness(image)
# brightness.enhance(1.5).save('brightness.jpg')


# sharpness = ImageEnhance.Sharpness(image)
# sharpness.enhance(1.5).save('sharpness.jpg')


# !/usr/bin/python

from PIL import Image, ImageTk
from tkinter import Tk
from tkinter.ttk import Frame, Label
import sys


class Example(Frame):

    def __init__(self):
        super().__init__()

        self.loadImage()
        self.initUI()

    def loadImage(self):
        try:
            self.img = Image.open("tatrs.jpg")

        except IOError:
            print("Unable to load image")
            sys.exit(1)

    def initUI(self):

        self.master.title("Label")

        tatras = ImageTk.PhotoImage(self.img)
        label = Label(self, image=tatras)

        # reference must be stored
        label.image = tatras

        label.pack()
        self.pack()

    def setGeometry(self):

        w, h = self.img.size
        self.master.geometry(("%dx%d+300+300") % (w, h))


def main():
    root = Tk()
    ex = Example()
    ex.setGeometry()
    root.mainloop()


if __name__ == '__main__':
    main()
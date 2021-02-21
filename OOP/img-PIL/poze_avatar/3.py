
from PIL import Image

class Image:
    # car_type = "Sedan"
    def __init__(self, name, img):
        self.name = name
        self.img = img

    def show():
        img = Image.open("../IMG/bmw-m235i-gran-coupe-016.jpg")
        new_name = "IMG/M2.jpg"
        img.save(new_name)

        img_M2 = Image.open("../IMG/M2.jpg")
        print(img.size)
        new_size = (250, 250)
        img_M2.thumbnail(new_size)
        img_M2.save("IMG/M2_thumbnail.jpg")
        return img_M2

x = Image("BMW_2", ("img/bmw-m235i-gran-coupe-016.jpg"))
print(x)

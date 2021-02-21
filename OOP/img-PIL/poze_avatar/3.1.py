
from PIL import Image

class Image():

    # def __init__(self, img, new_name_img, new_size_img, avatar_img):
    def __init__(self, img):
        self.img = img
        # self.new_name_img = new_name_img
        # self.new_size_img = new_size_img
        # self.avatar_img = avatar_img

    def show(self):
        # img = Image.open(input())   # img/source_photo/2.jpg
        img = Image.open("img/source_photo/2.jpg")

        print("Enter new_name_img: ", end="")
        n = input()
        new_name_img = "new_name_img/" + n + ".jpg"    # img/M2.jpg
        img.save(new_name_img)
        new_name_img = Image.open(new_name_img)
        # print(new_name_img, new_name_img.mode, new_name_img.size)
        print(new_name_img)


        # new_name_img = Image.open(new_name_img)
        new_size_img = (800, 600)
        new_name_img.thumbnail(new_size_img)
        new_name_img.save("new_size_img/" + n + ".jpg")
        # new_size_img = Image.open(new_size_img)
        print(new_size_img)



        # new_name_img = Image.open(new_name_img)
        avatar_img = (100, 100)
        new_name_img.thumbnail(avatar_img)
        new_name_img.save("avatar_img/" + n + "_thumbnail.jpg")
        # avatar_img = Image.open(avatar_img)
        print(avatar_img)


        return (avatar_img, new_size_img, new_name_img)

x = Image("img/source_photo/2.jpg")
print(x)

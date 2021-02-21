from PIL import Image

class Image1:

    def __init__(self, n):
        # self.img = img
        # self.new_name_img = new_name_img
        # self.new_size_img = new_size_img
        # self.avatar_img = avatar_img
        self.n = n

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

        return new_name_img

x = Image1()
print(x)
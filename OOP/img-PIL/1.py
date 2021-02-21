# import PIL
from PIL import Image

img = Image.open("IMG/bmw-m235i-gran-coupe-016.jpg")
new_name = "IMG/M2.jpg"
img.save(new_name)

img_M2 = Image.open("IMG/M2.jpg")
print(img.size)
new_size = (250, 250)
img_M2.thumbnail(new_size)
img_M2.save("IMG/M2_thumbnail.jpg")

# img_M2 = Image.open("M2.jpg")
# new_crop = (100, 100, 100, 100)
# img_M2_crop = img_M2.crop(new_crop)
# img_M2_crop_new_size = Image.new(color=0, size=(900, 900), mode="RGB")
# img_M2_crop_new_size.paste(img_M2_crop, (0, 0, 900, 900))
# img_M2_crop_new_size.save("M2_box.jpg")



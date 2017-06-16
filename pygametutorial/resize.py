import PIL
from PIL import Image

basewidth = 180
img = Image.open("vagon.jpg")
wpercent = (basewidth/ float(img.size[0]))
hsize = int((float(img.size[1]) * float(wpercent)))
img = img.resize((basewidth,hsize), PIL.Image.ANTIALIAS)
img.save('resized_image.jpg')

baseheight = 244
img = Image.open("vagon.jpg")
hpercent = (baseheight/ float(img.size[1]))
wsize = int((float(img.size[0]) * float(hpercent)))
img = img.resize((wsize,baseheight), PIL.Image.ANTIALIAS)
img.save('resized_image.jpg')


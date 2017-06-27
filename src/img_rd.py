# Import libraries
from PIL import Image

# Read image
#im = Image.open("../images/yellow.png")
im = Image.open("../images/test.jpg")
pix = im.load()
im_w, im_h = im.size

for h in xrange(im_h):
    for w in xrange(im_w):
        r,g,b = pix[w,h]
        #print r,g,b
        if (r > 150) and (g > 80) and (g < 150) and (b < 100):
            pix[w,h] = (255,255,0)
        else:
            pix[w,h] = (255,255,255)

im.save("alive_parrot.png") # Save the modified pixels as png

gry = im.convert('LA')
gry.save("grey.png")

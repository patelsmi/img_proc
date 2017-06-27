# Import libraries
from PIL import Image

# Read image
#im = Image.open("../images/yellow.png")
im = Image.open("../images/test.jpg")
pix = im.load()
im_w, im_h = im.size
delta = 2


for h in xrange(im_h):
    total = 0
    cnt = 0
    for w in xrange(im_w):
        r,g,b = pix[w,h]
        if (r > 150) and (g > 80) and (g < 150) and (b < 100):
            total = total + w
            cnt = cnt + 1
            #pix[w,h] = (r,g,b)
        else:
            pass
            #pix[w,h] = (255,255,255)
    if cnt is not 0:
        avg = total / cnt
    else:
        avg = 0
    for w in xrange(avg-delta,avg+delta,1):
        if avg is not 0:
            pix[w,h] = (0,0,0)

im.save("mean.png") # Save the modified pixels as png

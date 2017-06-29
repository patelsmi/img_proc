from PIL import Image
import numpy as np

def diff(in1, in2):
    return abs(in1 - in2)

def img_read(raw_image_path, out_image_path, ref_r, ref_g, ref_b, delta):
    im = Image.open(raw_image_path)
    pix = im.load()
    im_w, im_h = im.size

    for ht in np.arange(im_h):
        for wd in np.arange(im_w):
            r,g,b = pix[wd,ht]
            if (diff(r,ref_r)<delta) and (diff(g,ref_g)<delta) and (diff(b,ref_b)<delta):
                pix[wd,ht] = (255,255,0)
            else:
                pix[wd,ht] = (255,255,255)

    im.save(out_image_path)

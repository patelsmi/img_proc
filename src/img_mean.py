from PIL import Image
import numpy as np

def diff(in1, in2):
    return abs(in1 - in2)

def img_mean(raw_image_path, ref_r, ref_g, ref_b, delta):
    im = Image.open(raw_image_path)
    pix = im.load()
    im_w, im_h = im.size
    correction = im_w / 2
    drive_vector = {}

    for ht in np.arange(im_h):
        cnt = 0
        variation = 0
        for wd in np.arange(im_w):
            r,g,b = pix[wd,ht]
            if (diff(r,ref_r)<delta) and (diff(g,ref_g)<delta) and (diff(b,ref_b)<delta):
                variation += wd
                cnt += 1
        if cnt is 0:
            drive = correction
        else:
            drive = variation / cnt
        drive_vector[im_h - ht] = drive - correction

    print drive_vector

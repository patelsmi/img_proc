import helper_functions as hf
import img_calibrate as cal
import numpy as np

IMG_PATH = "../images/test4.jpg"


# Calibration
ref_r, ref_g, ref_b = cal.img_calibrate(IMG_PATH)
# print ref_r,ref_g,ref_b

# Real Time Processing
direction = []
img_handle = hf.get_img_handle(IMG_PATH)
img_pixels = hf.get_img_pixels(img_handle)
img_dimensions = hf.get_img_dimensions(img_handle)
img_ht = img_dimensions["height"]
img_wd = img_dimensions["width"]

row_indices = sorted(np.arange(img_ht), reverse=True)
for each_row in row_indices:
    row_pixs = hf.get_img_row(img_pixels,img_wd,each_row)
    row_variation = hf.get_row_variation(row_pixs,ref_r,ref_g,ref_b,100)
    direction.append(row_variation)

print direction




# DEBUG
# ref_r = 115
# ref_g = 159
#ref_b = 208
# hf.dbug_blacken_match_pixs(IMG_PATH, ref_r, ref_g, ref_b, 100)

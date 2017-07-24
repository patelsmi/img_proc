import helper_functions as hf
import img_calibrate as cal
import numpy as np

IMG_PATH1 = "../images/test4.jpg"
IMG_PATH2 = "../images/test3.jpg"

# Calibration
# ref_r, ref_g, ref_b = cal.img_calibrate(IMG_PATH)
# print ref_r,ref_g,ref_b
ref_r = 115
ref_g = 159
ref_b = 208


# Real Time Processing
img_handle1 = hf.get_img_handle(IMG_PATH1)
direction1 = hf.image_direction_vector(img_handle1,ref_r, ref_g, ref_b, 100)

img_handle2 = hf.get_img_handle(IMG_PATH2)
direction2 = hf.image_direction_vector(img_handle2,ref_r, ref_g, ref_b, 100)

result = hf.shift_and_add(direction1, direction2)

import helper_functions as hf
import img_calibrate as cal
import numpy as np

# Calibration
# ref_r, ref_g, ref_b = cal.img_calibrate(IMG_PATH)
# print ref_r,ref_g,ref_b
ref_r = 115
ref_g = 159
ref_b = 208

temp_image = '../images/test3.jpg'
result = [0]*792

img_handle = hf.get_img_handle(temp_image)
direction = hf.image_direction_vector(img_handle, ref_r, ref_g, ref_b,100)
result = hf.shift_and_add(result,direction)
if (result[0] < 0):
    print "left"
elif (result[0] > 0):
    print "right"
else:
    print "straight"



print result

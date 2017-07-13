import sys
import img_calibrate as cal
import img_read as rd

if len(sys.argv) is not 2:
    print "INCORRECT USAGE!!!  Pass image location as input."
    exit()

image_path = sys.argv[1]

ext = image_path.split(".")[-1]
tmp_image_path = image_path.replace(ext,"_tmp."+ext)
cal_r,cal_g,cal_b = cal.img_calibrate(image_path)

delta = 20

rd.img_read(\
        image_path,\
        tmp_image_path,\
        cal_r,\
        cal_g,\
        cal_b,\
        delta\
        )

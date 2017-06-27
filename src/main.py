import sys
import img_calibrate as cal

if len(sys.argv) is not 2:
    print "INCORRECT USAGE!!!  Pass image location as input."
    exit()

image_path = sys.argv[1]
print cal.img_calibrate(image_path)

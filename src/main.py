import helper_functions as hf
import img_calibrate as cal
import numpy as np
import camera as picam
import RPi.GPIO as GPIO

# Setup GPIOs
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Calibration
# ref_r, ref_g, ref_b = cal.img_calibrate(IMG_PATH)
# print ref_r,ref_g,ref_b
ref_r = 115
ref_g = 159
ref_b = 208

temp_image = '../images/latest.jpg'
result = [0]*792

# Real Time Processing
while True:
    input_switch = GPIO.input(17)
    if input_switch is True:
        # Capture Image
        image = picam.get_picture(temp_image)
        image_handle = hf.get_img_handle(temp_image)
        direction = hg.image_direction_vector(img_handle, ref_r, ref_g, ref_b,100)
        result = hf.shift_and_add(result,direction)
        if (result[0] < 0):
            print "left"
        elif (result[0] > 0):
            print "right"
        else:
            print "straight"
    else:
        print "Self Driving Mode Off"

import picamera as pic

def get_picture(img_path):
    camera = pic.PiCamera()
    camera.capture(img_path)

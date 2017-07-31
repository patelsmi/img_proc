from PIL import Image
import numpy as np
import picamera as pic

def get_img_handle(img_path):
    im = Image.open(img_path)
    return im

def get_img_pixels(img_handle):
    pixels = img_handle.load()
    return pixels

def get_img_dimensions(img_handle):
    img_w, img_h = img_handle.size
    return {"width": img_w, "height": img_h}

def get_img_row(pixels, row_len, row_idx):
    row_pix = []
    col_indices = np.arange(row_len)
    for col_idx in col_indices:
        row_pix.append(pixels[col_idx, row_idx])
    return row_pix

def check_pixel(r,g,b,ref_r,ref_g,ref_b,delta):
    r_valid = abs(ref_r - r) < delta
    g_valid = abs(ref_g - g) < delta
    b_valid = abs(ref_b - b) < delta
    if r_valid and g_valid and b_valid:
        return True
    else:
        return False

def get_row_variation(row_pixs, ref_r, ref_g, ref_b, delta):
    row_sum = 0
    row_count = 0
    for count,row_pix in enumerate(row_pixs):
        r,g,b = row_pix
        pix_valid = check_pixel(r,g,b,ref_r,ref_g,ref_b,delta)
        if pix_valid:
            row_sum += count
            row_count += 1
    if row_count:
        variation = (row_sum / row_count) - len(row_pixs)/2
    else:
        variation = 0
    return variation

def image_direction_vector(img_handle, ref_r,ref_g,ref_b,strictness):
    direction = []
    img_pixels = get_img_pixels(img_handle)
    img_dimensions = get_img_dimensions(img_handle)
    img_ht = img_dimensions["height"]
    img_wd = img_dimensions["width"]
    row_indices = sorted(np.arange(img_ht), reverse=True)
    for each_row in row_indices:
        row_pixs = get_img_row(img_pixels,img_wd,each_row)
        row_variation = get_row_variation(row_pixs,ref_r,ref_g,ref_b,strictness)
        direction.append(row_variation)
    return direction


def add_vectors(vector1,vector2):
    v1 = np.array(vector1)
    v2 = np.array(vector2)
    sum_vector = (v1 + v2)/2
    return list(sum_vector)

def shift_direction(vector):
    vector.pop(0)
    vector.append(0)
    return vector

def shift_and_add(vector1, vector2):
    shifted_vector = shift_direction(vector1)
    added_vector = add_vectors(shifted_vector, vector2)
    return added_vector

def get_picture(img_path):
    pic.capture(img_path)

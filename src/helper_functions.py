from PIL import Image
import numpy as np

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

def get_row_variation(row_pixs, ref_r, ref_g, ref_b, delta):
    row_sum = 0
    row_count = 0
    for count,row_pix in enumerate(row_pixs):
        r,g,b = row_pix
        r_valid = abs(ref_r - r) < delta
        g_valid = abs(ref_g - g) < delta
        b_valid = abs(ref_b - b) < delta
        if r_valid and g_valid and b_valid:
            row_sum += count
            row_count += 1
    if row_count:
        variation = (row_sum / row_count) - len(row_pixs)/2
    else:
        variation = 0
    return variation


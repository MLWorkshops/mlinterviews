"""
Utility functions.
By Micheleen Harris, 2021
MIT License
"""
import os
import matplotlib.pyplot as plt
import numpy as np


def pad_image(np_img):
    """Use numpy operations to add padding around an image in
    numpy format (an array of rank 3 - so 3 channels) in order
    to create a square image.
    
    Args
    ----
      np_img : numpy array
          image
    """

    h, w, c = np_img.shape
    side_len = max(h, w)
    # Create our square "palette" or area upon which the image data is placed
    # Make it kinda grey (e.g. a palette of all > 1)
    new_np_img = np.empty(side_len * side_len * c).reshape(
        side_len, 
        side_len, c)
    new_np_img.fill(255.)

    if h > w:
        for i in range(c):
            old_patch = np_img[:, :, i]
            pad = (side_len - w)//2
            new_np_img[:, pad:(pad + w), i] = old_patch
        return new_np_img
    elif w > h:
        for i in range(c):
            old_patch = np_img[:, :, i]
            pad = (side_len - h)//2
            new_np_img[pad:(pad + h), :, i] = old_patch
        return new_np_img
    else:
        # Image already square - lucky!
        return np_img

    




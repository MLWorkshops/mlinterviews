"""
Utility functions to use with image classification for ML Workshop.
By Micheleen Harris, 2021
MIT License
"""
import os
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image


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
    
def prep_images(img_dir):
    """
    Preprocess the images in the class folders
    1. Pad to square
    2. Resize to 64x64 pixels
    3. Save to new folder
    """
    image_files = []
    # Let's use only jpeg format images
    allowed_formats = ['jpeg', 'jpg']

    for root, subdirs, files in os.walk(img_dir):
        image_files += [os.path.join(root, file) for file in files \
                        if os.path.basename(file).split('.')[-1] in \
                        allowed_formats]
    
    print('Total number of images = ', len(image_files))
    
    # Make a new main folder
    new_folder = img_dir + '_64x64'
    print('Creating new main folder, ', new_folder)
    os.makedirs(new_folder, exist_ok=True)
    old_folder_basename = img_dir.split(os.sep)[-1]
    new_folder_basename = new_folder.split(os.sep)[-1]
    
    # Read, pad, resize and save new image to different folder
    for image_file in image_files:
        img = plt.imread(image_file)
        img = pad_image(img).astype(np.uint8)
        pil_img = Image.fromarray(img)
        pil_img = pil_img.resize((64,64))
        
        # Create class folder
        old_class_folder = os.path.dirname(image_file)
        new_class_folder = old_class_folder.replace(old_folder_basename,
                                                    new_folder_basename)
        os.makedirs(new_class_folder, exist_ok=True)
        new_name = image_file.replace(old_folder_basename,
                                      new_folder_basename)
        pil_img.save(new_name)

    




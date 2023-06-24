from skimage.morphology import dilation
from skimage.io import imread
import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import convolve2d

def multi_dilation(img, selem, n):
    """Do a successive dilation on the same image by n times."""
    for i in range(n):
        img = dilation(img, selem)
    return img

family = imread('anky_char.png')

gray_image = np.mean(family, axis=2)

kernel1 = np.array([[1, 2, 1],
                    [0, 0, 0],
                    [-1, -2, -1]])

conv_im1 = convolve2d(gray_image, kernel1, 'same')

kernel2 = np.array([[1, 0, -1],
                    [2, 0, -2],
                    [1, 0, -1]])

conv_im2 = convolve2d(gray_image, kernel2, 'same')

edge_image = np.sqrt(conv_im1**2 + conv_im2**2)

conv_im2 = convolve2d(gray_image, kernel2)

# Create a cross filter
selem = np.array([[0,1,0],
                  [1,1,1],
                  [0,1,0]])

# Perform dilation
darkened_image = multi_dilation(edge_image, selem, 1)

# Save the image (you can modify the cmap to change the color, for example 'binary' or 'gray')
plt.imsave('dilation_result_colored.png', darkened_image)

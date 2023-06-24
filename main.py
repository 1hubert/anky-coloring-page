"""This script is for creating a coloring book from a given image."""

from PIL import Image
import cv2
import numpy as np

# Load the image
image = Image.open('anky_char.png')

# Convert the image to grayscale
image = image.convert('L')

# Convert the PIL image to a NumPy array
image = np.array(image)

# Use the Canny edge detection algorithm to detect edges
edges = cv2.Canny(image, threshold1=60, threshold2=120)

# Dilate the edges to make them thicker
# play around with the iterations parameter to get the desired thickness
dilated_edges = cv2.dilate(edges, None, iterations=1)

# Invert the colors
coloring_book_image = cv2.bitwise_not(dilated_edges)

# Convert the NumPy array to a PIL image
coloring_book_image = Image.fromarray(coloring_book_image)

# Save the image
coloring_book_image.save('coloring_book_image.jpg')

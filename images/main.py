import streamlit as st
import numpy as np
import cv2
from PIL import Image

# Title of the web-app
st.title('Barcode Decoding with OpenCV')

# Uploading the images
img_file_buffer = st.file_uploader("Upload an image for decoding", type=["jpg", "jpeg", "png"])

def preprocess_image(image):
    # Convert the image to grayscale
    image = np.array(Image.open(img_file_buffer))
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Apply thresholding to convert to binary image
    _, binary = cv2.threshold(gray, 128, 255, cv2.THRESH_BINARY_INV)
    
    return binary

def find_start_and_end(binary_image):
    # Find the leftmost and rightmost non-zero pixel columns
    start_col = np.argmax(binary_image.sum(axis=0) > 0)
    end_col = binary_image.shape[1] - np.argmax(np.flip(binary_image.sum(axis=0)) > 0)
    
    return start_col, end_col

if img_file_buffer is not None:

  image = Image.open(img_file_buffer) # read image with PIL library
  st.image(image) #display

  binary_image = preprocess_image(img_file_buffer)
  st.image(binary_image)

  start_col, end_col = find_start_and_end(binary_image)
 

import streamlit as st
import numpy as np
import cv2
import functions
from PIL import Image

# Title of the web-app
st.title('Barcode Decoding with OpenCV')

# Uploading the images
img_file_buffer = st.file_uploader("Upload an image for decoding", type=["jpg", "jpeg", "png"])

if img_file_buffer is not None:

  image = Image.open(img_file_buffer) # read image with PIL library
  st.image(image) #display

  binary_image = functions.preprocess_image(img_file_buffer)

import streamlit as st
import numpy as np
import cv2
import functions

# Title of the web-app
st.title('Barcode Decoding with OpenCV')

# Uploading the images
img_file_buffer = st.file_uploader("Upload an image for decoding", type=["jpg", "jpeg", "png"])

if img_file_buffer is not None:
    display = cv2.open(str(img_file_buffer))
    st.image(display)

import streamlit as st
from PIL import Image
import numpy as np
import cv2
import easyocr

#title of the web-app
st.title('QR Code Decoding with OpenCV')

#uploading the images
img_file_buffer = st.file_uploader("Upload an image which you want to Decode", type=[ "jpg", "jpeg",'png'])

if img_file_buffer is not None:
    # Load the image
    image = cv2.imread(str(img_file_buffer))
    image = np.array(Image.open(img_file_buffer))
    st.subheader('Orginal Image')



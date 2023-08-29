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
    # Convert the uploaded image to a numpy array
    image = np.array(Image.open(img_file_buffer))

    st.subheader('Orginal Image')

    # Display the original image
    st.image(image, caption=f"Original Image", use_column_width=True)

    # Convert the image to RGB (EasyOCR uses RGB format)
    img_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Initialize EasyOCR Reader
    reader = easyocr.Reader(['en'])  # You can specify the languages you want to detect

    # Perform Text Detection
    results = reader.readtext(img_rgb)

    # Process OCR Results
    qr_codes = []
    for (bbox, text, prob) in results:
        if "http" in text:
            qr_codes.append(text)

    if qr_codes:
        st.subheader("Detected QR Codes:")
        for qr_code in qr_codes:
            st.write(qr_code)
    else:
        st.write("No QR codes detected.")

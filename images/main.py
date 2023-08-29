import streamlit as st
from PIL import Image
import numpy as np
import cv2
import easyocr

#title of the web-app
st.title('QR Code Decoding with OpenCV')

#uploading the images
img_file_buffer = st.file_uploader("Upload an image which you want to Decode", type=[ "jpg", "jpeg",'png'])


# Load the image
image = cv2.imread(img_file_buffer)





@st.cache
def qr_code_dec(image):
    
    decoder = cv2.QRCodeDetector()
    data, vertices, rectified_qr_code = decoder.detectAndDecode(image)

    return data
    """if len(data) > 0:
        print("Decoded Data: '{}'".format(data))

        # How to Decode

        # Show the detection in the image:
        show_qr_detection(image, vertices)
        rectified_image = np.uint8(rectified_qr_code)
        decoded_data = 'Decoded data: '+ data
        rectified_image = cv2.putText(rectified_image, decoded_data, (50, 350),
            fontFace=cv2.FONT_HERSHEY_COMPLEX, fontScale=2,
            color=(250, 225, 100), thickness=3, lineType=cv2.LINE_AA)
           
        return rectified_image  # Return the modified rectified_image instead of decoded_data

    return "No QR code detected" """


st.markdown("**Warning** Only add QR-code Images, other images will give out an error")

#uploading the images
img_file_buffer = st.file_uploader("Upload an image which you want to Decode", type=[ "jpg", "jpeg",'png'])

if img_file_buffer is not None:
    image = np.array(Image.open(img_file_buffer))
    st.subheader('Orginal Image')

    #display the image
    st.image(
        image, caption=f"Original Image", use_column_width=True
    ) 

    st.subheader('Decoded data')
    
    decoded_data = qr_code_dec(image)
    st.write(decoded_data)

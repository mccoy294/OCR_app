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

def decode_barcode(binary_image, start_col, end_col):
    # Decoding logic (simplified for example)
    barcode_data = ""
    
    # Assuming each bar is 3 pixels wide
    bar_width = 3
    for col in range(start_col, end_col, bar_width):
        bar_sum = binary_image[:, col:col+bar_width].sum()
        if bar_sum > binary_image.shape[0] * bar_width // 2:
            barcode_data += "1"
        else:
            barcode_data += "0"
    
    return barcode_data


def decode_code128(binary_data):
    # Mapping of patterns to characters for Code 128
    code128_chars = {
        "11011001100": "0", "11001101100": "1", "11001100110": "2",
        "10010011000": "3", "10010001100": "4", "10001001100": "5",
        "10011001000": "6", "10011000100": "7", "10001100100": "8",
        "11001001000": "9", "11001000100": "A", "11000100100": "B",
        "10110011100": "C", "10011011100": "D", "10011001110": "E",
        "10111001100": "F", "10011101100": "G", "10011100110": "H",
        "11001110010": "I", "11001011100": "J", "11001001110": "K",
        "11011100100": "L", "11001110100": "M", "11101101110": "N",
        "11101001100": "O", "11100101100": "P", "11100100110": "Q",
        "11101100100": "R", "11100110100": "S", "11100110010": "T",
        "11001111010": "U", "11001000010": "V", "11110001010": "W",
        "10100110000": "X", "10100001100": "Y", "10010110000": "Z",
        "10010000110": "FNC1", "10000101100": "FNC2", "10000100110": "FNC3",
        "10110010000": "FNC4", "10110000100": "SHIFT", "10001110110": "CODE_C",
        "10111011000": "CODE_B", "10111000110": "CODE_A", "11011010000": "START_A",
        "11011000010": "START_B", "11000110110": "START_C", "10100011000": "STOP",
    }

    # Lengths of different characters in Code 128
    code128_lengths = {
        "CODE_A": 2, "CODE_B": 2, "CODE_C": 2,
        "START_A": 4, "START_B": 4, "START_C": 4,
        "STOP": 4, "SHIFT": 8, "FNC1": 8, "FNC2": 8, "FNC3": 8, "FNC4": 8,
    }

    # Decoding logic
    decoded_text = ""
    while binary_data:
        # Get the next character pattern
        char_pattern = binary_data[:11]
        
        # Remove the processed pattern from the binary data
        binary_data = binary_data[11:]
        
        # Find the character from the mapping
        char = code128_chars.get(char_pattern)
        
        # If the character is found, add it to the decoded text
        if char:
            decoded_text += char
            
            # Skip characters based on their length
            char_length = code128_lengths.get(char, 6)
            binary_data = binary_data[char_length:]
        else:
            return "Invalid Code 128 barcode"

    return decoded_text


if img_file_buffer is not None:

  image = Image.open(img_file_buffer) # read image with PIL library
  st.image(image) #display

  binary_image = preprocess_image(img_file_buffer)
  st.image(binary_image)

  start_col, end_col = find_start_and_end(binary_image)

  barcode_data = decode_barcode(binary_image, start_col, end_col)
  st.write("Decoded Barcode Data:", barcode_data)

  # Assuming 'barcode_data' is the binary data obtained from the barcode
  barcode_text = decode_code128(barcode_data)
  st.write("Decoded Barcode Text:", barcode_text)
 

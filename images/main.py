import streamlit as st
from PIL import Image
import pytesseract
import functions.functions as fc

class OCR:

    def __init__(self):
        # Set the title of the page
        st.set_page_config(page_title="Invoice OCR")
        # Initialize the text option and set the analyze boolean to False
        self.text = ""
        self.analyze_text = False

    def initial(self):
        # Initial content of the page
        st.title("OCR Program")
        st.write("Optical Character Recognition (OCR) implemented with Python")
        image = st.file_uploader("Select an image", type=["png", "jpg"])
        # If an image is selected...
        if image:
            img = Image.open(image)
            st.image(img, width=350)
            st.info("Text extracted")
            self.text = self.extract_text(img)
            st.write("{}".format(self.text))

            # Option to analyze text
            self.analyze_text = st.sidebar.checkbox("Analyze text")
            if self.analyze_text == True:
                self.show_analysis()

    def extract_text(self, img):
        # The command that extracts the text from the image
        text = pytesseract.image_to_string(img, lang="eng")
        return text

    def show_analysis(self):
        # Searches for CPF, dates and good and bad words in the extraction
        cpf = fc.search_cpf(self.text)
        dates = fc.search_date(self.text)
        good_words, good_percentage = fc.search_good_words(self.text)
        bad_words, bad_percentage = fc.search_bad_words(self.text)

        if cpf is None:
            st.warning("No CPF found.")
        else:
            cpf = fc.summarize_cpf(cpf)
            st.success("CPF found:")
            st.write(cpf)

        if dates is None:
            st.warning("No dates found.")
        else:
            dates = fc.summarize_dates(dates)
            st.success("Dates found:")
            st.write(dates)

        if good_words == 0:
            st.warning("No good words found.")
        else:
            st.success("Good words:")
            st.write("{} word(s). Represent {:.2f}% of the words in the text.".format(good_words, good_percentage))

        if bad_words == 0:
            st.warning("No bad words found.")
        else:
            st.success("Bad words:")
            st.write("{} word(s). Represent {:.2f}% of the words in the text.".format(bad_words, bad_percentage))

ocr = OCR()
ocr.initial()

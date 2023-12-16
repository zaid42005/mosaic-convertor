import streamlit as st
import streamlit.components.v1 as components
import numpy as np
import cv2
from PIL import Image
import csv
import os
import pandas as pd

class Converter():
    def __init__(self) -> None:
        self.color_dict = {}

class Web():
    def __init__(self) -> None:
        self.draw_text()

    def draw_text(self):
        st.set_page_config(
            page_title="Pixelart-Converter",
            page_icon="🖼️",
            layout="centered",
            initial_sidebar_state="expanded",
        )
        st.title("PixelArt-Converter")
        self.upload = st.file_uploader("Upload Image", type=['jpg', 'jpeg', 'png', 'webp'])
        self.original, self.converted = st.columns(2)
        self.original.title("original img")
        self.converted.title("convert img")

if __name__ == "__main__":
    web = Web()
    converter = Converter()
    if web.upload != None:
        img = Image.open(web.upload)
        img = np.array(img)
        web.original.image(web.upload)
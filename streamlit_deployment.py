# -*- coding: utf-8 -*-
"""Streamlit Deployment.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1uen0wIsxkvapW37iMu9ot6R_aGu2Qfeq
"""
import streamlit as st
from PIL import Image
import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.vgg19 import VGG19
from tensorflow.keras.preprocessing.image import ImageDataGenerator

st.set_page_config(
    page_title="AI Generated Image",
    page_icon="🎨",
)

model = tf.keras.models.load_model("vgg19_model.h5")

map_dict = {0: 'AI Generated Image',
            1: 'Human Made',
            }

def main():
    img = None


    st.markdown(
        """
        <style>
        .rounded-heading {
            text-align: center;
            background: linear-gradient(to right, #ff6f61, #e23e57);
            color: white;
            padding: 23px;
            border-radius: 7px;
            box-shadow: 0px 3px 4px rgba(0, 0, 0, 0.2);
        }

        .rounded-heading:hover {
            background: linear-gradient(to left, #ff6f61, #e23e57);
        }
        </style>
        """,
        unsafe_allow_html=True
    )


    st.markdown("<h1 class='rounded-heading'>HueHarmony</h1>", unsafe_allow_html=True)

    st.markdown("<h3 style='text-align: center; color: #ff6f61; text-shadow: 0px 2px 5px rgba(0, 0, 0, 0.07);'>🎨 Image Palette Extractor</h3><br>", unsafe_allow_html=True)



    upload_tab, url_tab = st.tabs(["Upload", "Image URL"])
    with upload_tab:

        img_file = st.file_uploader("Upload an image", key="file_uploader", type=["jpg", "jpeg", "png"])
        if img_file is not None:
            img = Image.open(img_file).convert("RGB")
    if st.session_state.get("image_url"):
            st.warning("To use the file uploader, remove the image URL first.")

    with url_tab:

        url = st.text_input("Image URL", key="image_url")
        if url != "":
            try:
                response = requests.get(url)
                img = Image.open(BytesIO(response.content)).convert("RGB")
            except:
                st.error("The URL is not valid.")

Generate_pred = st.button("Generate Prediction")
if Generate_pred:
  prediction = model.predict(img_reshape).argmax()
  st.title("Predicted Label for the image is {}".format(map_dict [prediction]))

if __name__ == '__main__':
    main()


# -*- coding: utf-8 -*-
import streamlit as st
from PIL import Image
import numpy as np
import requests
import tensorflow as tf
from tensorflow.keras.losses import BinaryCrossentropy
from tensorflow.keras.optimizers import Adam
import joblib
from PIL import Image
import pandas as pd
import time


st.set_page_config(
    page_title="AI Generated Image Detection",
    page_icon="🖼️",
)

model = tf.keras.models.load_model('cnn_skfcv_model.h5')

map_dict = {0: 'AI-Generated Image',
            1: 'Human Made',
            }

def preprocess_image(image):
    """Preprocess the image to the format required by the model"""
    resized = image.resize((224, 224))  # Resize the image to the input shape expected by the model
    image_array = np.array(resized)  # Convert image to numpy array
    image_array = image_array / 255.0  # Normalize pixel values
    image_array = np.expand_dims(image_array, axis=0)  # Add batch dimension
    return image_array

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
    st.markdown(
        "<h1 class='rounded-heading'>AI Generated Detection</h1>", 
        unsafe_allow_html=True)

    st.markdown("---")
    
    # Test out some of our images
    st.subheader("Give it a try!")
    st.write("Do you have a cool picture but not sure it is made by Human or AI? Our model can correctly identify Image generated by AI or Not with roughly 91% accuracy. Try it now!!")
    
    # Load your Bird images (replace these paths with your actual file paths)
    image_paths = [".streamlit/AI_Generated_1.jpg", ".streamlit/Human_Made_1.jpg", ".streamlit/AI_Generated_2.jpg", ".streamlit/Human_Made_2.jpg"]

    # Function to resize the image to a specified width and height -> for display purposes only
    def resize_image(image_path, width, height):
        image = Image.open(image_path)
        resized_image = image.resize((width, height))
        return resized_image
    
    # Specify the width and height for resizing
    image_width = 400
    image_height = 400
    
    # Use st.columns to create columns corresponding to the number of images we have uploaded for trial
    columns = st.columns(len(image_paths))
    
    # Mapping of image indices to results
    results_mapping = {
        1: "AI Generated",
        2: "Human Made",
        3: "AI Generated",
        4: "Human Made"
    }

    # Display each image in a column with a "Detect" button underneath
    for idx, (column, image_path) in enumerate(zip(columns, image_paths)):
        # Resize the image
        resized_image = resize_image(image_path, image_width, image_height)
        
        # Display the resized image with the specified width and center it
        column.image(resized_image, caption=f"Image {idx + 1}", use_column_width=True)
        
        # Add a "Detect" button centered below the image
        if column.button(f"Detect Image {idx + 1}"):
            # Display the spinner animation while processing
            with st.spinner(f"Results are loading for image {idx + 1}..."):
                # Simulate model processing time (replace with your actual detection logic)
                time.sleep(1)
        
                # Your detection logic goes here
                result = results_mapping.get(idx + 1, "Prediction Error")  
        
                # Display the result
                column.write(f"{result}")
    
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

    if img is not None:
        img_array = preprocess_image(img)
        img = Image.open(img_file)
        st.image(img, caption="Uploaded Image.")

    Generate_pred = st.button("Generate Prediction")
    if Generate_pred:
        try:
            prediction = round(model.predict(img_array)[0][0])
            st.subheader("Your Image Predicted as {}".format(map_dict[prediction]))
        except Exception as e:
            st.error(f"An error occurred during prediction: {e}")



st.sidebar.title('About Project')
st.sidebar.write("This project focused on detecting and classifying AI-Generated and Human-Made images using a CNN. The project employs Stratified K-Fold Cross-Validation (SKFCV) to improve model evaluation and reduce overfitting.")

# Sidebar - Project More Info
st.sidebar.subheader('More About This Project')
notebook_url = "https://colab.research.google.com/drive/12QHrg2vToyw0KzcQ1lY8UrxMF92wIGYu?usp=sharing"
dataset_url = "https://www.kaggle.com/datasets/macayanpioloc/ai-generated-and-human-made-painting/data"

notebook_markdown = f'[Notebook]({notebook_url})'
dataset_markdown = f'[Dataset]({dataset_url})'

st.sidebar.markdown(f"{notebook_markdown}", unsafe_allow_html=True)
st.sidebar.markdown(f"{dataset_markdown}", unsafe_allow_html=True)

# Sidebar - Bio info
st.sidebar.title('About Me:')
linkedin_url = "https://www.linkedin.com/in/sayyidah-amalia-rokhimah/"
github_url = "https://github.com/sayyidahbisa"
medium_url = "https://medium.com/@sayyidah"

linkedin_markdown = f'[LinkedIn]({linkedin_url})'
github_markdown = f'[GitHub]({github_url})'
medium_markdown = f'[Blog]({medium_url})'

st.sidebar.subheader('Sayyidah Amalia Rokhimah')
st.sidebar.markdown(f"{linkedin_markdown} | {github_markdown} | {medium_markdown}", unsafe_allow_html=True)
st.sidebar.write('sayyidahbisabikin@gmail.com')
        
if __name__ == '__main__':
    main()

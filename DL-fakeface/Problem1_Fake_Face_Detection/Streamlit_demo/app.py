import streamlit as st
import tensorflow as tf
from PIL import Image
import numpy as np

# Define a function to load a model
@st.cache(allow_output_mutation=True)
def load_model(model_name):
    if model_name == 'RNN Model':
        model_path = 'models/custom_cnn_model.h5'
    elif model_name == 'Transfer Model v1':
        model_path = 'models/transfer_model_v1.h5'
    elif model_name == 'Transfer Model v2':
        model_path = 'models/transfer_model_v2.h5'
    return tf.keras.models.load_model(model_path)

# Streamlit interface
st.title('Image Classification with Deep Learning')
st.write('Upload an image and select a model to classify the image.')

# Upload an image
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])
if uploaded_file is not None:
    image = Image.open(uploaded_file).convert('RGB')
    st.image(image, caption='Uploaded Image', use_column_width=True)
    image = image.resize((224, 224))  # Adjust size depending on your model's input
    image = np.array(image)
    image = image / 255.0  # Normalize the image
    image = np.expand_dims(image, axis=0)

# Model selection
model_option = st.selectbox(
    'Select a Model',
    ('RNN Model', 'Transfer Model v1', 'Transfer Model v2')  # Add more models as needed
)

if st.button('Classify Image'):
    if uploaded_file is not None:
        # Load and predict
        model = load_model(model_option)
        prediction = model.predict(image)

        # Display the numerical prediction value
        st.write(f'Prediction probability (REAL): {float(prediction):.4f}')

        if prediction > 0.5:
            st.success('The photo is REAL.')
        else:
            st.error('The photo is FAKE.')
    else:
        st.error('Please upload an image to classify.')


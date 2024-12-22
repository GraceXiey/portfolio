import streamlit as st
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import model_from_json
import cv2

# Load model structure
with open('model.json', 'r') as json_file:
    loaded_model_json = json_file.read()

# Load model weights
model = model_from_json(loaded_model_json)
model.load_weights("model_weights.weights.h5")

# Compile the model (required after loading)
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# Function to load, preprocess, and save the image
def load_and_preprocess_image(uploaded_file, save_path='resized_image.jpg'):
    # Read the image file
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    img = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)
    
    # Resize the image to 48x48 pixels
    resized_img = cv2.resize(img, (48, 48))
    
    # Save the resized image
    cv2.imwrite(save_path, resized_img)
    
    # Convert image to RGB (OpenCV uses BGR by default)
    resized_img_rgb = cv2.cvtColor(resized_img, cv2.COLOR_BGR2RGB)
    
    # Normalize the image
    img_array = resized_img_rgb / 255.0  # rescale image values
    img_array = np.expand_dims(img_array, axis=0)  # add batch dimension
    return img_array

# Mapping of model output to class names (adjust this to match your model's classes)
class_names = ['angry', 'disgust', 'fear', 'happy', 'sad', 'surprise', 'neutral']  # replace with your actual class names

# Streamlit UI
st.title("Image Classification App")
st.write("Upload an image to classify")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Display the uploaded image
    st.image(uploaded_file, caption='Uploaded Image', use_column_width=True)
    st.write("")
    st.write("Classifying...")

    # Load and preprocess the image
    img_array = load_and_preprocess_image(uploaded_file)

    # Predict the class of the image
    prediction = model.predict(img_array)
    st.write(f"Prediction array: {prediction}")  # Debugging line to check the prediction array
    st.write(f"Class names length: {len(class_names)}")  # Debugging line to check class names length
    st.write(f"Prediction shape: {prediction.shape}")  # Debugging line to check prediction shape

    predicted_index = np.argmax(prediction)
    st.write(f"Predicted index: {predicted_index}")  # Debugging line to check the predicted index

    # Ensure the predicted index is within the range of class names
    if predicted_index < len(class_names):
        predicted_class = class_names[predicted_index]
        st.write(f"Predicted class: {predicted_class}")
        st.write(f"Confidence: {np.max(prediction):.2f}")
    else:
        st.write("Error: Predicted index is out of range.")

# To run the app, use the following command in the terminal:
# streamlit run app.py

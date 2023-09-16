import streamlit as st
from tensorflow.keras.preprocessing import image
from tensorflow.keras.models import load_model

from PIL import Image
import numpy as np
st.title("Image Classification")

st.write("Predict the Corn disease Image.")

model = load_model("Model.h5")
labels=['Blight', 'Common_Rust', 'Gray_Leaf_Spot', 'Healthy']
uploaded_file = st.file_uploader(
    "Upload an image taken by Corn Disease:", type="jpg"
)
predictions=-1
if uploaded_file is not None:
    image1 = Image.open(uploaded_file)
    image1=image.smart_resize(image1,(255,255))
    image1=classi=np.array(image1)/255.
    result=model.predict(image1[np.newaxis,...])
    
    label=labels[np.argmax(result)]
  

st.write("### Prediction Result")
if st.button("Predict"):
    if uploaded_file is not None:
        image1 = Image.open(uploaded_file)
        st.image(image1, caption="Uploaded Image", use_column_width=True)
        st.markdown(
            f"<h2 style='text-align: center;'>Image of {label}</h2>",
            unsafe_allow_html=True,
        )
    else:
        st.write("Please upload file or choose sample image.")


st.write("If you would not like to upload an image, you can use the sample image instead:")
sample_img_choice = st.button("Use Sample Image")

if sample_img_choice:
    image1 = Image.open("sample.jpg")
    image1=image.smart_resize(image1,(255,255))
    img_array = image.img_to_array(image1)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = img_array/255.0
    predictions = model.predict(img_array)
    label=labels[np.argmax(predictions)]
    image1 = Image.open("sample.jpg")
    st.image(image1, caption="Uploaded Image", use_column_width=True)    
    st.mark
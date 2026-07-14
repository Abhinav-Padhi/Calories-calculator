import streamlit as st
import requests
from PIL import Image

st.title("Food Detection")

uploaded = st.file_uploader("Upload an Image", type=["jpg", "png", "jpeg"])

if uploaded:
    st.image(uploaded)

    if st.button("Predict"):
        files = {"file": uploaded.getvalue()}

        response = requests.post(
            "http://127.0.0.1:8000/predict",
            files=files
        )

        if response.status_code == 200:
            st.json(response.json())
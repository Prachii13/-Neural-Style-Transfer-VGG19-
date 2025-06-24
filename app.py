import streamlit as st
from PIL import Image
import style_transfer

st.title("🎨 Neural Style Transfer")

content = st.file_uploader("Upload content image", type=["jpg", "png"])
style = st.file_uploader("Upload style image", type=["jpg", "png"])

if content and style:
    with open("content.jpg", "wb") as f: f.write(content.read())
    with open("style.jpg", "wb") as f: f.write(style.read())

    st.image("content.jpg", caption="Content Image", width=200)
    st.image("style.jpg", caption="Style Image", width=200)

    if st.button("Stylize"):
        style_transfer.main()  # Runs the script
        st.image("stylized.jpg", caption="🖼️ Stylized Output")

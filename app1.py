import streamlit as st
import pytesseract
from PIL import Image, ImageOps

st.title("Reconocimiento Óptico de Caracteres")

img_file_buffer = st.camera_input("Toma una Foto")

with st.sidebar:
    filtro = st.radio("Aplicar Filtro", ('Con Filtro', 'Sin Filtro'))

if img_file_buffer is not None:
    image = Image.open(img_file_buffer)
    
    if filtro == 'Con Filtro':
        image_to_process = ImageOps.invert(image.convert('RGB'))
    else:
        image_to_process = image

    text = pytesseract.image_to_string(image_to_process)
    
    st.write("### Texto detectado:")
    st.write(text)

    



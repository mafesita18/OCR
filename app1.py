import streamlit as st
import pytesseract
from PIL import Image, ImageOps

st.title("Reconocimiento Óptico de Caracteres")

img_file_buffer = st.camera_input("Toma una Foto")

with st.sidebar:
    filtro = st.radio("Aplicar Filtro", ('Con Filtro', 'Sin Filtro'))

if img_file_buffer is not None:
    # Cargar la imagen directamente con PIL
    image = Image.open(img_file_buffer)
    
    # Aplicar filtro de inversión si se selecciona
    if filtro == 'Con Filtro':
        # Convierte a RGB si es necesario y luego invierte colores
        image_to_process = ImageOps.invert(image.convert('RGB'))
    else:
        image_to_process = image

    # Aplicar OCR directamente sobre la imagen de PIL
    text = pytesseract.image_to_string(image_to_process)
    
    st.write("### Texto detectado:")
    st.write(text)

    



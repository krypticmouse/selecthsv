import cv2
import numpy as np
import streamlit as st
from PIL import Image

st.set_page_config(page_title = 'HSV Value Selector')
st.title("HSV Selector")
img_buffer = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])

if img_buffer is not None:
    img = np.array(Image.open(img_buffer))

    st.subheader('Uploaded Image:-')
    st.image(img, width = 400)

    mi,ma = st.beta_columns(2)
    miv,mav = st.beta_columns(2)

    h_min = st.slider('Minimum Hue', 0, 179, 0)
    h_max = st.slider('Maximum Hue', 0, 179, 179)
    s_min = st.slider('Minimum Saturation', 0, 255, 0)
    s_max = st.slider('Maximum Saturation', 0, 255, 255)
    v_min = st.slider('Minimum Value', 0, 255, 0)
    v_max = st.slider('Minimum Value', 0, 255, 255)

    mi.subheader('HSV Min Values:-')
    ma.subheader('HSV Max Values:-')

    miv.text(f'[{h_min},{s_min},{v_min}]')
    mav.text(f'[{h_max},{s_max},{v_max}]')

    imgHSV = cv2.cvtColor(img,cv2.COLOR_RGB2HSV)
    lower = np.array([h_min, s_min, v_min])
    upper = np.array([h_max, s_max, v_max])
    mask = cv2.inRange(imgHSV,lower,upper)
    color = cv2.bitwise_and(img,img,mask = mask)

    c1,c3 = st.beta_columns(2)
    i1,i3 = st.beta_columns(2)

    c1.subheader('Image Mask:-')
    i1.image(mask, width = 350)

    c3.subheader('Extracted Image:-')
    i3.image(color, width = 350)
pass

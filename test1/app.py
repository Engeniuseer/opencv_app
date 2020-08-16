import streamlit as st
import cv2
import numpy as np


@st.cache(allow_output_mutation=True)
def init():
    return cv2.VideoCapture(0)


def main():
    cap=init() 

    st.title('OPENCV APP 😎')
    frameST = st.empty()

    option = st.sidebar.selectbox('Select your option:',  ('RGB', 'Gray', 'BGR', 'Gaussian', 'Canny'))
    gaussian = st.sidebar.empty()
    canny=st.sidebar.empty()
    canny2=st.sidebar.empty()

    if option=='Canny':
        c_x=canny.slider('X:',0,150,75)
        c_y=canny2.slider('Y:',70,250,120)
    else:
        canny.empty()
        canny2.empty()
        c_x=75
        c_y=120


    while True:
        ret, frame = cap.read()
        if option=='RGB':
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        elif option=='Gray':
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        elif option=='Gaussian':
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            frame = cv2.GaussianBlur(frame,(5,5),0)
        elif option=='Canny':
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            frame = cv2.Canny(frame,c_x,c_y)
        frameST.image(frame)
        
if __name__=="__main__":
    main()
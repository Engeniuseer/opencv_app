import streamlit as st
import cv2
import numpy as np
from keras.models import load_model


@st.cache(allow_output_mutation=True)
def init(cascPath):
    return cv2.CascadeClassifier(cascPath),cv2.VideoCapture(0)

cascPath='haarcascade_frontalface_default.xml'
faceCascade,cap=init(cascPath) 
st.title('OPENCV APP 😎')
frameST = st.empty()
faceST=st.empty()

option = st.sidebar.selectbox('Select your option:',('RGB','Gray','BGR','Gaussian','Edge Detection','FaceDetection'))
gaussian = st.sidebar.empty()
canny=st.sidebar.empty()
canny2=st.sidebar.empty()
face=st.sidebar.empty()


color_dict={'Blue':(0,0,255),'Green':(0,255,0),'Red':(255,0,0),'Orange':(200,100,0),'Yellow':(255,255,0)}

if option=='Gaussian':
    sig=gaussian.slider('Sigma:',-25,25,3)
else:
    gaussian.empty()
    std=0
    
if option=='Edge Detection':
    c_x=canny.slider('X:',0,150,75,key=1)
    c_y=canny2.slider('Y:',70,250,120,key=2)
else:
    canny.empty()
    canny2.empty()
    c_x=75
    c_y=120
    
if option=='FaceDetection':
    color=face.selectbox('Select color:',  ('Blue', 'Green', 'Red', 'Orange', 'Yellow'))
else:
    color='Blue'
    face.empty()
    
        
while True:
    ret, frame = cap.read()
    if option=='RGB':
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    elif option=='Gray':
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    elif option=='FaceDetection':
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = faceCascade.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=10,
            minSize=(100, 100),
        )
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), color_dict[color], 2)
    elif option=='Gaussian':
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame = cv2.GaussianBlur(frame,(5,5),sig)
    elif option=='Edge Detection':
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame = cv2.Canny(frame,c_x,c_y)
    
    
    frameST.image(frame)

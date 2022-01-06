import cv2
import streamlit as st

st.write("""# Hello Sopon""")
run = st.checkbox('Run')
FRAME_WINDOW = st.image([])
camera = cv2.VideoCapture(0)
#img = cv2.imread("Aeroplane.jpg")
#img = img[:,:,::-1]
while (run):
    ret, frame = camera.read()    
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    FRAME_WINDOW.image(frame)
else:
    st.write('Stopped')

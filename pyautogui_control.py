import cv2
import mediapipe as mp
import numpy as np
import pyautogui
from module_tracking import Hand_tracking

##Walter Captura de Vídeo pela Webcam
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1920) #Matheus (Zoom máximo que consegui sem deformar) 19/10/22
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080) #Matheus (Zoom máximo que consegui sem deformar) 19/10/22

pyautogui.FAILSAFE = False

#Walter Loop do código
while True:
    sucess, img = cap.read()
    list_coord = Hand_tracking(img)
    ix, iy = list_coord[0]
    pyautogui.moveTo(ix, iy)

import cv2
import mediapipe as mp
import time
import numpy as np

cap = cv2.VideoCapture(0)
canvas = None
x1,y1=0,0



mpHands = mp.solutions.hands
hands = mpHands.Hands(max_num_hands=1)
mpDraw = mp.solutions.drawing_utils

pTime = 0
cTime = 0
while (1):
    sucess, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    if canvas is None:
        canvas = np.zeros_like(img)
    results = hands.process(imgRGB)
    #print(results.multi_hand_landmarks)
    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            lm = handLms.landmark[8]
            #for id, lm in enumerate(handLms.landmark):
                #print(id,lm)
            h, w, c = img.shape
            cx, cy = int(lm.x *w), int(lm.y*h)
             #if id ==0:
            cv2.circle(img, (cx,cy), 7, (0 , 255, 0), cv2.FILLED)
            if x1 == 0 and y1 == 0:
                x1, y1 = cx, cy
            else:
                canvas = cv2.line(canvas, (x1, y1), (cx, cy), [255, 0, 0], 4)
            x1, y1 = cx, cy

    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)

    img = cv2.add(img, canvas)
    stacked = np.hstack((canvas, img))
    cv2.imshow('VIRTUAL PEN', cv2.resize(stacked, None, fx=0.6, fy=0.6))

    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break
    if k == ord('c'):
        canvas = None

cv2.destroyAllWindows()
cap.release()

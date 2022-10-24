'''
Walter Guilherme Candeia
'''


import cv2
import mediapipe as mp
import time

class Detector():
    def __init__(self, modo = False, NumMaos = 1, CtzDeteccao = 0.5, CtzMapeamento = 0.5):
        self.modo = modo
        self.NumMaos = NumMaos
        self.CtzDeteccao = CtzDeteccao
        self.CtzMapeamento = CtzMapeamento

        self.mpMaos = mp.solutions.hands
        self.Maos = self.mpMaos.Hands(self.modo, self.NumMaos, self.CtzDeteccao, self.CtzMapeamento)
        self.mpDesenho = mp.solutions.drawing_utils

    def EncontPosi(self, img, SMao = 0, draw = True):

        Ptlist = []
        if self.results.multi_hand_landmarks:
            myMao = self.results.multi_hand_landmarks[SMao]
            for id, pt in enumerate(myMao.landmark):
                h, w, c = img.shape
                cx, cy = int(pt.x * w), int(pt.y * h)
                Ptlist.append([id, cx, cy])
                if draw:
                    cv2.circle(img, (cx, cy), 7, (255, 0, 255), cv2.FILLED)
        return Ptlist

    def EncontMaos(self,img, draw = True):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.Maos.process(imgRGB)

        if self.results.multi_hand_landmarks:
            for maospts in self.results.multi_hand_landmarks:
                if draw:
                    self.mpDesenho.draw_landmarks(img, maospts, self.mpMaos.HAND_CONNECTIONS)
        return img
    
def main():
    pTime = 0
    cTime = 0
    cap = cv2.VideoCapture(0)
    detector = Detector()

    while True:
        success, img = cap.read()
        img = detector.EncontMaos(img)
        Ptlist = detector.EncontPosi(img)
        if len(Ptlist) != 0:
            print(Ptlist[4])

        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime

        cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)

        cv2.imshow("Image", img)
        cv2.waitKey(1)



if __name__ == "__main__":
    main()

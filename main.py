import cv2
import mediapipe as mp
import time
import numpy as np
from tracking_module import Hand_tracking

##Walter Captura de Vídeo pela Webcam
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280) #Matheus (Zoom máximo que consegui sem deformar) 19/10/22
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1280) #Matheus (Zoom máximo que consegui sem deformar) 19/10/22

#Walter Criação da variável da segunda tela onde será impresso a escrita
quadro = None

#Walter Declaração de valores
x1, y1 = 0, 0
pTime = 0
cTime = 0

#Walter Loop do código
while True:
    sucess, img = cap.read()  #Walter Leitura da imagem
    img = cv2.flip(img, 1)  #Walter Inversão da imagem no eixo Y
    list_coord = Hand_tracking(img)
    ix , iy = list_coord[0]
    px, py = list_coord[1]
    mdx, mdy = list_coord[2]
    cv2.circle(img, (px, py), 7, (0, 255, 0), cv2.FILLED)  #Walter Desenho do círculo sob a falange do Polegar
    cv2.circle(img, (ix, iy), 7, (0, 255, 0), cv2.FILLED)  #Walter Desenho do círculo sob a falange do Indicador
    pinca = (ix - px) ** 2 + (iy - py) ** 2 <= 300  #Walter Variável do tipo booleano que define se o gesto Pinça está ativado ou não.
    pinca_medio = (px - mdx) ** 2 + (py - mdy) ** 2 <= 175  # Matheus (Alterei a função de apagar fazendo a pinça com o dedo médio) (Tambem alterei o nome da variável para ficar mais coeso) 19/10/22
    #Walter Loop do Desenho
    if not pinca:
        x1, y1 = 0, 0
    else:
        if x1 == 0 and y1 == 0:
            x1, y1 = ix, iy
        else:
            quadro = cv2.line(quadro, (x1, y1), (ix, iy), [255, 255, 255], 2)
            x1, y1 = ix, iy
    if pinca_medio:  # Matheus (Apaga o que já foi desenhado
        quadro = np.zeros_like(img)

    #Walter Leitura e impressão do FPS
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)

    img = cv2.add(img, quadro)  #Walter Coloca a imagem Canvas como continuação da Captura
    reposicao = np.hstack((quadro, img))  #Walter Sobrepõe os frames
    cv2.imshow('Air Writing',cv2.resize(reposicao, None, fx=0.6, fy=0.6))  # Imprimi as imagens na tela,(resize, redimensiona as telas)

    #Walter Impede que o programa rode em loop infinito sem sobreposição de frames
    w = cv2.waitKey(1) & 0xFF
    if w == 27:
        break
    if w == ord('c'):
        canvas = None
#Walter Fecha a Janela de impressão
cv2.destroyAllWindows()
cap.release()

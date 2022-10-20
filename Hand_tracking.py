import cv2
import mediapipe as mp
import time
import numpy as np

#Walter (Captura de Vídeo pela Webcam)
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280) #Matheus (Zoom máximo que consegui sem deformar) 19/10/22
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1280) #Matheus (Zoom máximo que consegui sem deformar) 19/10/22

#Walter (Criação da variável da segunda tela onde será impresso a escrita)
canvas = None

x1, y1 = 0, 0

#Walter (Chamando os modulos de detecção do Mediapipe)
mpHands = mp.solutions.hands
hands = mpHands.Hands(max_num_hands=1)
mpDraw = mp.solutions.drawing_utils

pTime = 0
cTime = 0

#Walter (Loop do código)
while True:
    sucess, img = cap.read()  #Walter (Leitura da imagem)
    img = cv2.flip(img, 1)  #Walter (Inversão da imagem no eixo Y
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  #Walter (Setando a leitura da imagem no formato RGB
    if canvas is None:
        canvas = np.zeros_like(img)  #Walter (Criação da segunda tela semelhante a "img"
    results = hands.process(imgRGB)  #Walter (Mapeamento das mãos sob a captura(RGB)
    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            pontamindinho = handLms.landmark[20]  #Walter (Definição da variável do Dedo Polegar sob suas coordenadas(x, y, z)
            pontaanelar= handLms.landmark[16]  #Walter (Definição da variável do Dedo Polegar sob suas coordenadas(x, y, z)
            pontamédio = handLms.landmark[12]  #Walter (Definição da variável do Dedo Polegar sob suas coordenadas(x, y, z)
            pontaindicador = handLms.landmark[8]  #Walter (Definição da variável do Dedo Indicador sob suas coordenadas(x, y, z)
            pontapolegar = handLms.landmark[4]  #Walter (Definição da variável do Dedo Polegar sob suas coordenadas(x, y, z)
            basemindinhho= handLms.landmark[17]  #Walter (Definição da variável do Dedo Polegar sob suas coordenadas(x, y, z)
            baseanelar = handLms.landmark[13]  #Walter (Definição da variável do Dedo Polegar sob suas coordenadas(x, y, z)
            basemédio = handLms.landmark[9]  #Walter (Definição da variável do Dedo Indicador sob suas coordenadas(x, y, z)
            baseindicador = handLms.landmark[5]  #Walter (Definição da variável do Dedo Polegar sob suas coordenadas(x, y, z)
            #print(dedo1)
            # for id, lm in enumerate(handLms.landmark):
            h, w, c = img.shape
            ix, iy = int(pontaindicador.x * w), int(pontaindicador.y * h)  #Walter (Filtragem das coordenadas da ponta do indicador
            px, py = int(pontapolegar.x * w), int(pontapolegar.y * h)  #Walter (Filtragem das coordenadas da ponta do polegar
            mdx, mdy = int(pontamédio.x * w), int(pontamédio.y * h)  #Walter (Filtragem das coordenadas da base do polegar
            ax, ay = int(pontaanelar.x * w), int(pontaanelar.y * h)  #Walter (Filtragem das coordenadas da falnge medial do indicador
            mx, my = int(pontamindinho.x * w), int(pontamindinho.y * h)  #Walter (Filtragem das coordenadas da ponta do indicador
            bix, biy = int(baseindicador.x * w), int(baseindicador.y * h)  #Walter (Filtragem das coordenadas da ponta do indicador
            bmdx, bmdy = int(basemédio.x * w), int(basemédio.y * h)  #Walter (Filtragem das coordenadas da base do polegar
            bax, bay = int(baseanelar.x * w), int(baseanelar.y * h)  #Walter (Filtragem das coordenadas da falnge medial do indicador
            bmx, bmy = int(basemindinhho.x * w), int(basemindinhho.y * h)  #Walter (Filtragem das coordenadas da ponta do indicador
            # if id ==0:
            cv2.circle(img, (px, py), 7, (0, 255, 0), cv2.FILLED)  #Walter (Desenho do círculo sob a falange do Polegar
            cv2.circle(img, (ix, iy), 7, (0, 255, 0), cv2.FILLED)  #Walter (Desenho do círculo sob a falange do Indicador
            pinca = (ix - px) ** 2 + (iy - py) ** 2 <= 300  #Walter (Variável do tipo booleano que define se o gesto Pinça está ativado ou não.
            pinca_medio = (px-mdx) ** 2 + (py - mdy) ** 2 <= 175 #Matheus (Alterei a função de apagar fazendo a pinça com o dedo médio) (Tambem alterei o nome da variável para ficar mais coeso) 19/10/22
            #Walter (Loop do Desenho
            if not pinca:
                x1, y1 = 0, 0
            else: #Walter (Começa a desenhar se pinça for verdadeiro
                if x1 == 0 and y1 == 0:
                    x1, y1 = ix, iy
                else:
                    canvas = cv2.line(canvas, (x1, y1), (ix, iy), [255, 255, 255], 2)
                    x1, y1 = ix, iy
            if pinca_medio: #Matheus (Apaga o que já foi desenhado
                canvas = np.zeros_like(img)


    #Walter (Leitura e impressão do FPS
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)

    img = cv2.add(img, canvas)  #Walter (Coloca a imagem Canvas como continuação da Captura
    stacked = np.hstack((canvas, img))  #Walter (Sobrepõe os frames
    cv2.imshow('Air Writing',cv2.resize(stacked, None, fx=0.6, fy=0.6))  #Walter (Imprimi as imagens na tela,(resize, redimensiona as telas)

    #Walter (Impede que o programa rode em loop infinito sem sobreposição de frames
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break
    if k == ord('c'):
        canvas = None
#Walter (Fecha a Janela de impressão
cv2.destroyAllWindows()
cap.release()

import cv2
import mediapipe as mp
def Hand_tracking(img):
    mpMaos = mp.solutions.hands
    Maos = mpMaos.Hands(max_num_hands=1)
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  #Walter Setando a leitura da imagem no formato RGB
    results = Maos.process(imgRGB)  #Walter Mapeamento das mãos sob a captura(RGB)
    if results.multi_hand_landmarks:
        for maospts in results.multi_hand_landmarks:
            pontamédio = maospts.landmark[12]  #Walter Definição da variável do Dedo Polegar sob suas coordenadas(x, y, z)
            pontaindicador = maospts.landmark[8]  #Walter Definição da variável do Dedo Indicador sob suas coordenadas(x, y, z)
            pontapolegar = maospts.landmark[4]  #Walter Definição da variável do Dedo Polegar sob suas coordenadas(x, y, z)
            #print(dedo1)
            # for id, lm in enumerate(handLms.landmark):
            h, w, c = img.shape
            ix, iy = int(pontaindicador.x * 1920), int(pontaindicador.y * 1080)  #Walter Filtragem das coordenadas da ponta do indicador
            px, py = int(pontapolegar.x * w), int(pontapolegar.y * h)  #Walter Filtragem das coordenadas da ponta do polegar
            mdx, mdy = int(pontamédio.x * w), int(pontamédio.y * h)  #Walter Filtragem das coordenadas da base do polegar
            list_coord = [(ix, iy), (px, py), (mdx, mdy)]
    return list_coord

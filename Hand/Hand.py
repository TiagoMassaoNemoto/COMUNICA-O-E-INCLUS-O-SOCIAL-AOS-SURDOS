import mediapipe as mp
import cv2
import numpy as np
from os import listdir, path

custom_color_1 = (102, 22, 21)
custom_color_2 = (21,22,102)

mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands

#pegando os nomes dos frames
name_image = (i for i in listdir("C:\\Users\\timas\\Desktop\\Pratica\\Alfabeto\\Z"))
#pegando um nome da lista
with mp_hands.Hands(
    static_image_mode=True,
    max_num_hands=2,
    min_detection_confidence=0.5) as hands:
    
    for image in name_image:
        
        img = cv2.imread("C:\\Users\\timas\\Desktop\\Pratica\\Alfabeto\\Z\\" + image)

        results = hands.process(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
        
        if not results.multi_hand_landmarks:
            continue
        
        image_height, image_width, _ = img.shape
        
        annotated_image = img.copy()
        annotated_image2 = img.copy()
    
        for hand_landmarks in results.multi_hand_landmarks:
                        
            mp_drawing.draw_landmarks(
                annotated_image,
                hand_landmarks,
                mp_hands.HAND_CONNECTIONS,
                #azul escuro
                mp_drawing.DrawingSpec(color=custom_color_1, thickness=2),
                mp_drawing.DrawingSpec(color=custom_color_1, thickness=2))

            mp_drawing.draw_landmarks(
                annotated_image2,
                hand_landmarks,
                mp_hands.HAND_CONNECTIONS,
                #vermelho escuro
                mp_drawing.DrawingSpec(color=custom_color_2, thickness=2),
                mp_drawing.DrawingSpec(color=custom_color_2, thickness=2))
            
            #transformando em hsv as imagens com mediapipe azul/vermelho
            hsv = cv2.cvtColor(annotated_image, cv2.COLOR_BGR2HSV)
            hsv2 = cv2.cvtColor(annotated_image2, cv2.COLOR_BGR2HSV)

            #colocando as cores a ser filtrada
            #azul
            lower_color1 = np.array([110,100,50])
            upper_color1 = np.array([135,255,255])

            #vermelho
            lower_color2 = np.array([0,100,50])
            upper_color2 = np.array([10,255,255])

            #aplicando filtro de cor
            mask1 = cv2.inRange(hsv, lower_color1, upper_color1)

            result1 = cv2.bitwise_and(annotated_image, annotated_image, mask = mask1)

            mask2 = cv2.inRange(hsv2, lower_color2, upper_color2)

            result2 = cv2.bitwise_and(annotated_image2, annotated_image2, mask = mask2)
            
            #juntando as duas imagens filtrada azul/vermelho
            junction = cv2.addWeighted(result1,0.7,result2,0.7,0)
            
            #cor roxa a ser filtrada da junction
            lower_color3 = np.array([148,160,85])
            upper_color3 = np.array([150,163,87])

            hsv3 = cv2.cvtColor(junction, cv2.COLOR_BGR2HSV)
            
            mask3 = cv2.inRange(hsv3, lower_color3, upper_color3)

            result3 = cv2.bitwise_and(junction, junction, mask = mask3)            

            #salvamento da filtragem da imagem com mediapipe
            cv2.imwrite(image ,result3)

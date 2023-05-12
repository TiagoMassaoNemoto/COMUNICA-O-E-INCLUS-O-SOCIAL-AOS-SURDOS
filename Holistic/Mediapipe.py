import mediapipe as mp
import cv2
import numpy as np
from os import listdir, path

mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_holistic = mp.solutions.holistic

custom_color_1 = (102, 22, 21)
custom_color_2 = (21,22,102)

#pegando os nomes dos frames
name_image = (i for i in listdir("C:\\Users\\timas\\Desktop\\Pratica\\Teste Frame"))
#pegando um nome da lista
for image in name_image:
    img = cv2.imread("C:\\Users\\timas\\Desktop\\Pratica\\Teste Frame\\" + image)
    BG_COLOR = (192, 192, 192) # gray
    with mp_holistic.Holistic(
        static_image_mode=True,
        model_complexity=2,
        enable_segmentation=True,
        refine_face_landmarks=True) as holistic:
        image_height, image_width, _ = img.shape
        # Convert the BGR im o RGB before processing.
        results = holistic.process(cv2.cvtColor(img,cv2.COLOR_BGR2RGB))

        # if results.pose_landmarks:
        #     print(w
        #         f'Nose coordinates: ('
        #         f'{results.pose_landmarks.landmark[mp_holistic.PoseLandmark.NOSE].x * image_width}, '
        #         f'{results.pose_landmarks.landmark[mp_holistic.PoseLandmark.NOSE].y * image_height})'
        #     )

        annotated_image = img.copy()
        annotated_image2 = img.copy()
        
        # Draw segmentation on the image.
        # To improve segmentation around boundaries, consider applying a joint
        # bilateral filter to "results.segmentation_mask" with "image".
        condition = np.stack((results.segmentation_mask,) * 3, axis=-1) > 0.1
        bg_image = np.zeros(img.shape, dtype=np.uint8)
        bg_image[:] = BG_COLOR
        annotated_image = np.where(condition, annotated_image, bg_image)
        annotated_image2 = np.where(condition, annotated_image2, bg_image)
        # Draw pose, left and right hands, and face landmarks on the image.
        
        #Configuração do Holistic e Hand na cor azul e vermelho
        mp_drawing.draw_landmarks(
            annotated_image,
            results.face_landmarks,
            mp_holistic.FACEMESH_TESSELATION,
            #azul escuro
            mp_drawing.DrawingSpec(color=custom_color_1, thickness=2),
            mp_drawing.DrawingSpec(color=custom_color_1, thickness=2),
            )
        mp_drawing.draw_landmarks(
            annotated_image2,
            results.face_landmarks,
            mp_holistic.FACEMESH_TESSELATION,
            mp_drawing.DrawingSpec(color=custom_color_2, thickness=2),
            mp_drawing.DrawingSpec(color=custom_color_2, thickness=2),
            )
        
        mp_drawing.draw_landmarks(
            annotated_image,
            results.pose_landmarks,
            mp_holistic.POSE_CONNECTIONS,
            #azul escuro
            mp_drawing.DrawingSpec(color=custom_color_1, thickness=2),
            mp_drawing.DrawingSpec(color=custom_color_1, thickness=2),
            )
        mp_drawing.draw_landmarks(
            annotated_image2,
            results.pose_landmarks,
            mp_holistic.POSE_CONNECTIONS,
            #vermelho escuro
            mp_drawing.DrawingSpec(color=custom_color_2, thickness=2),
            mp_drawing.DrawingSpec(color=custom_color_2, thickness=2),
            )
        
        mp_drawing.draw_landmarks(
            annotated_image,
            results.right_hand_landmarks,
            mp_holistic.HAND_CONNECTIONS,
            #azul escuro
            mp_drawing.DrawingSpec(color=custom_color_1, thickness=2),
            mp_drawing.DrawingSpec(color=custom_color_1, thickness=2),
            )
        mp_drawing.draw_landmarks(
            annotated_image2,
            results.right_hand_landmarks,
            mp_holistic.HAND_CONNECTIONS,
            #vermelho escuro
            mp_drawing.DrawingSpec(color=custom_color_2, thickness=2),
            mp_drawing.DrawingSpec(color=custom_color_2, thickness=2),
            )
        
        mp_drawing.draw_landmarks(
            annotated_image,
            results.left_hand_landmarks,
            mp_holistic.HAND_CONNECTIONS,
            #azul escuro
            mp_drawing.DrawingSpec(color=custom_color_1, thickness=2),
            mp_drawing.DrawingSpec(color=custom_color_1, thickness=2),
            )
        mp_drawing.draw_landmarks(
            annotated_image2,
            results.left_hand_landmarks,
            mp_holistic.HAND_CONNECTIONS,
            #vermelho escuro
            mp_drawing.DrawingSpec(color=custom_color_2, thickness=2),
            mp_drawing.DrawingSpec(color=custom_color_2, thickness=2),
            )
        # Plot pose world landmarks.
        # mp_drawing.plot_landmarks(
        #     results.pose_world_landmarks, mp_holistic.POSE_CONNECTIONS)
        
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
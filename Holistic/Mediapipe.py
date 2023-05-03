import mediapipe as mp
import cv2
import numpy as np
from os import listdir, path

mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_holistic = mp.solutions.holistic
#pegando os nomes dos frames
name_image = (i for i in listdir("C:\\Users\\timas\\Desktop\\Pratica\\Teste Frame"))
#pegando nome do frame um por um
for image in name_image:
    #variavel com o frame
    img = cv2.imread("C:\\Users\\timas\\Desktop\\Pratica\\Teste Frame\\" + image)
    #cor do background
    BG_COLOR = (192, 192, 192) # gray
    #configurações mediapipe
    with mp_holistic.Holistic(
        static_image_mode=True,
        model_complexity=2,
        enable_segmentation=True,
        refine_face_landmarks=True) as holistic:
        image_height, image_width, _ = img.shape
        # Convert the BGR im o RGB before processing.
        results = holistic.process(cv2.cvtColor(img,cv2.COLOR_BGR2RGB))

        # if results.pose_landmarks:
        #     print(
        #         f'Nose coordinates: ('
        #         f'{results.pose_landmarks.landmark[mp_holistic.PoseLandmark.NOSE].x * image_width}, '
        #         f'{results.pose_landmarks.landmark[mp_holistic.PoseLandmark.NOSE].y * image_height})'
        #     )

        annotated_image = img.copy()
        # Draw segmentation on the image.
        # To improve segmentation around boundaries, consider applying a joint
        # bilateral filter to "results.segmentation_mask" with "image".
        condition = np.stack((results.segmentation_mask,) * 3, axis=-1) > 0.1
        bg_image = np.zeros(img.shape, dtype=np.uint8)
        bg_image[:] = BG_COLOR
        annotated_image = np.where(condition, annotated_image, bg_image)
        # Draw pose, left and right hands, and face landmarks on the image.
        mp_drawing.draw_landmarks(
            annotated_image,
            results.face_landmarks,
            mp_holistic.FACEMESH_TESSELATION,
            landmark_drawing_spec=None,
            connection_drawing_spec=mp_drawing_styles
            .get_default_face_mesh_tesselation_style())
        mp_drawing.draw_landmarks(
            annotated_image,
            results.pose_landmarks,
            mp_holistic.POSE_CONNECTIONS,
            landmark_drawing_spec=mp_drawing_styles.
            get_default_pose_landmarks_style())
        # Plot pose world landmarks.
        # mp_drawing.plot_landmarks(
        #     results.pose_world_landmarks, mp_holistic.POSE_CONNECTIONS)
        #salvamento do frame com mediapipe implantado
        cv2.imwrite(image,annotated_image)

import cv2
import os
import mediapipe as mp
import numpy as np

def main():
    # Crie uma pasta para salvar os frames (caso ela não exista)
    
    #⚠️⚠️⚠️colocar o nome da pasta que estara os frames⚠️⚠️⚠️⚠️
    #               👇👇👇👇 ex: 'letra A'
    output_folder = "frames"  # Substitua pelo caminho desejado
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Inicialize a captura de vídeo da câmera do notebook
    cap = cv2.VideoCapture(0)  # 0 representa a câmera padrão do computador

    # Verificar se a câmera foi aberta corretamente
    if not cap.isOpened():
        print("Não foi possível abrir a câmera.")
        return

    count = 0
    fps = 3  # Taxa de frames a serem salvos

    # Inicialize o MediaPipe Hands
    mp_drawing = mp.solutions.drawing_utils
    mp_hands = mp.solutions.hands
    hands = mp_hands.Hands(static_image_mode=True)
    
    custom_color_1 = (102, 22, 21)
    custom_color_2 = (21,22,102)

    while True:
        # Capturar o próximo frame da câmera
        ret, frame = cap.read()

        # Verificar se o frame foi capturado corretamente
        if not ret:
            print("Falha ao capturar o quadro de vídeo.")
            break

        # Processar o frame usando o MediaPipe Hands
        image_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = hands.process(image_rgb)
        
        annotated_image = image_rgb.copy()
        annotated_image2 = image_rgb.copy()

        if results.multi_hand_landmarks:
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
    

            # Salvar o frame a cada fps frames
            if count % fps == 0:
                #⚠️⚠️⚠️colocar o nome que da foto⚠️⚠️⚠️ 👇👇👇👇👇👇 ex: 'frame-letra_A%d.jpg'
                frame_name = os.path.join(output_folder, 'frame-x%d.jpg' % (count // fps))
                cv2.imwrite(frame_name, result3)

            count += 1

            # Mostrar o frame capturado em uma janela
            cv2.imshow('Camera', result3)

            # Sair do loop ao pressionar a tecla 'q'
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    # Liberar recursos
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()

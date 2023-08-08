import cv2
import mediapipe as mp
import numpy as np
import tensorflow as tf

# Carregue o modelo do TensorFlow feito no código redeneural
model = tf.keras.models.load_model('C:\\Users\\timas\\Downloads\\modelo_letras')  # Substitua pelo caminho correto do modelo

def classify_as_letter(image):
    # Pré-processar a imagem (exemplo simples de redimensionamento)
    image = cv2.resize(image, (28, 28))  # Redimensione para o tamanho esperado pelo modelo

    # Converta a imagem para escala de cinza, se necessário
    if len(image.shape) == 3:
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Expanda as dimensões para se adequar ao modelo (adicionar dimensão do lote e canal)
    image = image.reshape(1, 28, 28, 1)

    # Classificar a imagem usando o modelo do TensorFlow
    prediction = model.predict(image)
    class_index = np.argmax(prediction[0])

    # Defina as classes que você treinou no modelo (todas as letras do alfabeto)
    classes = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    return classes[class_index]

# Resto do código permanece inalterado...

def main():
    # Inicialize a captura de vídeo da câmera
    cap = cv2.VideoCapture(0)  # 0 representa a câmera padrão do computador

    # Verificar se a câmera foi aberta corretamente
    if not cap.isOpened():
        print("Não foi possível abrir a câmera.")
        return

    custom_color_1 = (102, 22, 21)
    custom_color_2 = (21,22,102)

    # Inicialize o MediaPipe Hands
    mp_drawing = mp.solutions.drawing_utils
    mp_hands = mp.solutions.hands
    mp_drawing_styles = mp.solutions.drawing_styles
    hands = mp_hands.Hands(static_image_mode=False, max_num_hands=2)

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

        # Se houver mãos detectadas na imagem, classifique a imagem
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
                # Obter as coordenadas da caixa delimitadora da mão
                x_min = int(min(hand_landmarks.landmark, key=lambda landmark: landmark.x).x * frame.shape[1])
                y_min = int(min(hand_landmarks.landmark, key=lambda landmark: landmark.y).y * frame.shape[0])
                x_max = int(max(hand_landmarks.landmark, key=lambda landmark: landmark.x).x * frame.shape[1])
                y_max = int(max(hand_landmarks.landmark, key=lambda landmark: landmark.y).y * frame.shape[0])

                
                
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

            # Processar a imagem da mão detectada
            hand_image = frame[y_min:y_max, x_min:x_max]

            # Classificar a imagem
            class_predicted = classify_as_letter(result3)
            
            # Exibir a classificação na imagem
            cv2.putText(frame, class_predicted, (x_min, y_min), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

        # Mostrar o frame capturado em uma janela
        cv2.imshow('Camera', frame)

        # Sair do loop ao pressionar a tecla 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Liberar recursos
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
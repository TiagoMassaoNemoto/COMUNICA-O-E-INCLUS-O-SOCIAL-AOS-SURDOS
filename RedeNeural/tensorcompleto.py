import cv2
import mediapipe as mp
import numpy as np
import tensorflow as tf

# Carregue o modelo do TensorFlow feito no código redeneuralcompleto
model = tf.keras.models.load_model('C:\\Users\\Caioe\\Downloads\\COMUNICACAO-E-INCLUSAO-SOCIAL-AOS-SURDOS-main\\modelo_letra_alfabeto')  # Substitua pelo caminho correto do modelo

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

def main():
    # Inicialize a captura de vídeo da câmera
    cap = cv2.VideoCapture(0)  # 0 representa a câmera padrão do computador

    # Verificar se a câmera foi aberta corretamente
    if not cap.isOpened():
        print("Não foi possível abrir a câmera.")
        return

    # Inicialize o MediaPipe Hands
    mp_drawing = mp.solutions.drawing_utils
    mp_hands = mp.solutions.hands
    hands = mp_hands.Hands(static_image_mode=False, max_num_hands=1)

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

        # Se houver mãos detectadas na imagem, classifique a imagem
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                # Obter as coordenadas da caixa delimitadora da mão
                x_min = int(min(hand_landmarks.landmark, key=lambda landmark: landmark.x).x * frame.shape[1])
                y_min = int(min(hand_landmarks.landmark, key=lambda landmark: landmark.y).y * frame.shape[0])
                x_max = int(max(hand_landmarks.landmark, key=lambda landmark: landmark.x).x * frame.shape[1])
                y_max = int(max(hand_landmarks.landmark, key=lambda landmark: landmark.y).y * frame.shape[0])

                # Processar a imagem da mão detectada
                hand_image = frame[y_min:y_max, x_min:x_max]

                # Classificar a imagem
                class_predicted = classify_as_letter(hand_image)
                
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
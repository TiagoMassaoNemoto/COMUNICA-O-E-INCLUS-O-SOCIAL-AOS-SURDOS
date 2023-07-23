import cv2
import os
import numpy as np
import tensorflow as tf
from sklearn.model_selection import train_test_split # Importa a função train_test_split do scikit-learn, que é usada para dividir o conjunto de dados em conjuntos de treinamento e teste

# Função para carregar as imagens do conjunto de dados
def load_images_from_folder(folder):
    images = []
    labels = []
    for label, class_folder in enumerate(os.listdir(folder)):
        class_path = os.path.join(folder, class_folder)
        for filename in os.listdir(class_path):
            img_path = os.path.join(class_path, filename)
            img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
            if img is not None:
                img = cv2.resize(img, (28, 28))
                images.append(img)
                labels.append(label)
    return np.array(images), np.array(labels)

# Carregar as imagens e rótulos do conjunto de dados
data_folder = "C:\\Users\\Caioe\\OneDrive\\Documentos\\imagens C"  # Substitua pelo caminho correto do seu conjunto de dados
images, labels = load_images_from_folder(data_folder)

# Pré-processar as imagens
images = images.reshape(-1, 28, 28, 1)  # Adicionar dimensão do canal
images = images / 255.0

# Dividir o conjunto de dados em treinamento e teste (80% treinamento, 20% teste)
train_images, test_images, train_labels, test_labels = train_test_split(images, labels, test_size=0.2, random_state=42)

# Criar a arquitetura da rede neural convolucional
model = tf.keras.Sequential([
    tf.keras.layers.Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)),
    tf.keras.layers.MaxPooling2D((2, 2)),
    tf.keras.layers.Conv2D(64, (3, 3), activation='relu'),
    tf.keras.layers.MaxPooling2D((2, 2)),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(64, activation='relu'),
    tf.keras.layers.Dense(2, activation='softmax')  # 2 unidades de saída para as classes 'A' e 'C'
])

# Compilar o modelo
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# Treinar o modelo
model.fit(train_images, train_labels, epochs=10, batch_size=32, validation_split=0.1)

# Avaliar o desempenho do modelo usando o conjunto de teste
test_loss, test_accuracy = model.evaluate(test_images, test_labels)
print("Acurácia no conjunto de teste:", test_accuracy)

model.save('modelo_letras')
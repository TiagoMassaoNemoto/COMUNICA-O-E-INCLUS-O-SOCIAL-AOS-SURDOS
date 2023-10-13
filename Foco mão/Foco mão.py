import cv2
import mediapipe as mp
# import pyttsx
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands

#captura da imagem da webcam
cap = cv2.VideoCapture(0)

count = 0

#mapeamento das mãos
with mp_hands.Hands(
    model_complexity=0,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5) as hands:
  while cap.isOpened():
    success, img = cap.read()
    img.flags.writeable = True
    frameRGB = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    results = hands.process(frameRGB)
    handsPoints = results.multi_hand_landmarks
    h, w, _ = img.shape
    if handsPoints != None:
        for hand in handsPoints:
            x_max = 0
            y_max = 0
            x_min = w
            y_min = h
            for lm in hand.landmark:
                x, y = int(lm.x * w), int(lm.y * h)
                if x > x_max:
                    x_max = x
                if x < x_min:
                    x_min = x
                if y > y_max:
                    y_max = y
                if y < y_min:
                    y_min = y
            #processo para focar na mão, tirando as variaveis profundidade e localização
            x_value = (-(x_min) + (x_max))*0.1
            y_value = (-(y_min) + (y_max))*0.1
            x_min = int(x_min-x_value)
            y_min = int(y_min-y_value)
            x_max = int(x_max+x_value)
            y_max = int(y_max+y_value)
            img = cv2.rectangle(img, (x_min, y_min), (x_max, y_max), (0, 255, 0), 2)
            imgCut = img[y_min:y_max,x_min:x_max]
            imgCut = cv2.resize(imgCut,(224,224))
            
        
        try:
            cv2.imshow('Mao',imgCut)
            
        except:
            continue
                    
    cv2.imshow('Imagem',img)
    cv2.waitKey(1)
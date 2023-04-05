import cv2

video = "C:\\Users\\timas\\Videos\\Captures\\Introdução.mkv"

cap = cv2.VideoCapture(video)
count = 0
#"controla a quantidade de frame a salvar"
fps = 10

while cap.isOpened():

    res, frame = cap.read()
    frame_name = 'frame-%d.jpg' %(count/fps)
    #controla a quantidade de frame a salvar
    if count % fps == 0:
        cv2.imwrite(frame_name,frame)
    count += 1
    
cap.release()

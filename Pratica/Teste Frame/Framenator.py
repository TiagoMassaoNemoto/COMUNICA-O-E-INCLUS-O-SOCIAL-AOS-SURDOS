import cv2
#pasta onde esta o video
video = "C:\\Users\\timas\\Videos\\Captures\\Introdução.mkv"
#variavel com o video
cap = cv2.VideoCapture(video)
count = 0
#"variavel que controla a quantidade de frame a salvar"
fps = 10

while cap.isOpened():
#separado os frames do video
    res, frame = cap.read()
    #controla a quantidade de frame a salvar
    frame_name = 'frame-%d.jpg' %(count/fps)
    #verifica se ainda tem frame para salvar
    if str(type(frame)) == "<class 'NoneType'>":
        break
    #salva os frames
    if count % fps == 0:
        cv2.imwrite(frame_name,frame)
    count += 1
cap.release()

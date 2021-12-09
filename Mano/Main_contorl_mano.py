import cv2.cv2
from cvzone.HandTrackingModule import *
from cvzone.SerialModule import SerialObject

# Generamos la captura de video con CV2
cap = cv2.VideoCapture(0)  # El orden de las webcam va del 0 a n (siendo n el numero de camaras que tenga)
detector = HandDetector(detectionCon=0.8, maxHands=1)  # Funcion para deteccion de manos de CvZone
mySerial = SerialObject("COM3", 9600, 1)  # Iniciamos comunicacion serial entre mi arduino y el programa
fondo = cv2.imread("Vangogh.jfif")

while True:
    # Obtenemos la imagen para trabajar con ella
    success, img = cap.read()
    hands, img = detector.findHands(img)
    if hands:
        hand = hands[0]
        lmList = hand["lmList"]  # Lista de 21 landmarks
        bbox = hand["bbox"]  # Bounding box info x,y,w,h
        handType1 = hand["type"]  # Handtype Left or Right

        fingers = detector.fingersUp(hand)
        mySerial.sendData(fingers)
        print(fingers)

        totalFingers = fingers.count(1)
        cv2.putText(img, "Dedo UP %s" %str(totalFingers), (bbox[0] + 100, bbox[1] - 30),
                        cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 2)

    img = cv2.resize(img, (900, 500))
    cv2.imshow("Image", img)
    cv2.waitKey(1)



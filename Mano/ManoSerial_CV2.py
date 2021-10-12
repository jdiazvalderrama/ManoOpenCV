"""
Autor: Javier Alonso Diaz Valderrama

Universidad de Valparaiso
javier.diazv@alumnos.uv.cl

Estaba aburrido, si le encuentran alguna funcion a la mano, de pana jasjjda yo no le veo ninguna :D
"""

from cvzone.HandTrackingModule import *
from cvzone.SerialModule import SerialObject


cap = cv2.VideoCapture(0)
detector = HandDetector(maxHands=1, detectionCon=0.7)
mySerial = SerialObject("COM3", 9600, 1)

while True:
    success, img = cap.read()
    img = detector.findHands(img)
    lmList, bbox = detector.findPosition(img)

    if lmList:
        dedo = detector.fingersUp()
        print(dedo)
        mySerial.sendData(dedo)

    cv2.imshow("Imagen", img)
    cv2.waitKey(1)

import cv2
from cvzone.HandTrackingModule import *
from cvzone.SerialModule import SerialObject
import serial

cap = cv2.VideoCapture(1)
detector = HandDetector(detectionCon=0.8, maxHands=1)
mySerial = SerialObject("COM3", 9600, 1)

while True:
    # Get image frame
    success, img = cap.read()
    hands, img = detector.findHands(img)
    if hands:
        # Hand 1
        hand1 = hands[0]
        lmList1 = hand1["lmList"]  # List of 21 Landmark points
        bbox1 = hand1["bbox"]  # Bounding box info x,y,w,h
        centerPoint1 = hand1['center']  # center of the hand cx,cy
        handType1 = hand1["type"]  # Handtype Left or Right

        fingers1 = detector.fingersUp(hand1)
        mySerial.sendData(fingers1)

    cv2.imshow("Image", img)
    cv2.waitKey(1)
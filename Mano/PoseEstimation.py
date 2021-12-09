from cvzone.HandTrackingModule import *
import cv2
import mediapipe as mp
import time

mpDraw = mp.solutions.drawing_utils
mpPose = mp.solutions.pose
pose = mpPose.Pose()
detector = HandDetector(detectionCon=0.8, maxHands=2)
width = 1280
height = 720

cap = cv2.VideoCapture(0)
fondo = cv2.imread("negro.jfif")

pTime = 0
while True:
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = pose.process(imgRGB)
    # print(results.pose_landmarks)
    if results.pose_landmarks:
        mpDraw.draw_landmarks(fondo, results.pose_landmarks, mpPose.POSE_CONNECTIONS)
        for id, lm in enumerate(results.pose_landmarks.landmark):
            h, w, c = fondo.shape
            print(id, lm)
            cx, cy = int(lm.x * w), int(lm.y * h)
            cv2.circle(fondo, (cx, cy), 5, (255, 0, 0), cv2.FILLED)



    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    cv2.putText(fondo, str(int(fps)), (70, 50), cv2.FONT_HERSHEY_PLAIN, 3,
                (255, 0, 0), 3)

    img = cv2.resize(img, (width, height))
    fondo = cv2.resize(fondo, (width, height))

    cv2.imshow("Image", fondo)
    cv2.imshow("Imagen2", img)
    cv2.waitKey(1)
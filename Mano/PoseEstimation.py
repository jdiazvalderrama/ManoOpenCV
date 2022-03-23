import cv2
import mediapipe as mp
import time

mpDraw = mp.solutions.drawing_utils
mpPose = mp.solutions.pose
pose = mpPose.Pose()
width = 600
height = 400

cap = cv2.VideoCapture(0)
pTime = 0

r = 255
g = 255
b = 255

while True:
    fondo = cv2.imread("persp.jpg")

    success, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = pose.process(imgRGB)
    # print(results.pose_landmarks)
    if results.pose_landmarks:
        mpDraw.draw_landmarks(fondo, results.pose_landmarks, mpPose.POSE_CONNECTIONS, mpDraw.DrawingSpec(color=(245,117,66), thickness=4, circle_radius=2),
                              mpDraw.DrawingSpec(color=(r, g, b), thickness=8, circle_radius=4))
        for id, lm in enumerate(results.pose_landmarks.landmark):
            h, w, c = fondo.shape
            #print(id, lm)
            cx, cy = int(lm.x * w), int(lm.y * h)
            cv2.circle(fondo, (cx, cy), 5, (255, 0, 0), cv2.FILLED)

    """r += 6
    g += 6
    b -= 6

    if r >= 255:
        r = 0
    if g >= 255:
        g = 0
    if b > 255:
        b = 0"""

    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    cv2.putText(fondo, str(int(fps)), (70, 50), cv2.FONT_HERSHEY_PLAIN, 3,
                (255, 0, 0), 3)

    img = cv2.resize(img, (width, height))
    fondo = cv2.resize(fondo, (width, height))

    cv2.imshow("Image", fondo)
    cv2.imshow("Imagen2", img)
    cv2.waitKey(10)
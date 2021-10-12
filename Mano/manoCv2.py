import cv2
import mediapipe as mp

cap = cv2.VideoCapture(0)
mpHands = mp.solutions.hands
hands = mpHands.Hands(max_num_hands=1)
mpDraw = mp.solutions.drawing_utils


while True:
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    #print(results.multi_hand_landmarks)

    if results.multi_hand_landmarks:
        for i in results.multi_hand_landmarks:
            for id, lm in enumerate(i.landmark):
                #print(id, lm)
                h, w, c = img.shape
                cx, cy = int(lm.x*w), int(lm.y*h)
                print(id, cx, cy)
                if id in (4, 8, 12, 16, 20):
                    cv2.circle(img, (cx, cy), 10, (255, 0, 100), cv2.FILLED)



            mpDraw.draw_landmarks(img, i, mpHands.HAND_CONNECTIONS)


    cv2.imshow("Imagen", img)
    cv2.waitKey(1)

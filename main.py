import cv2
from hand_tracking import HandDetector
from gesture_logic import GestureRecognizer
from controls import Controller

W, H = 640, 480

cap = cv2.VideoCapture(0)
cap.set(3, W)
cap.set(4, H)

detector = HandDetector()
recognizer = GestureRecognizer()
controller = Controller(W, H)

while True:
    success, img = cap.read()
    if not success:
        break

    img = cv2.flip(img, 1)

    img = detector.find_hand(img)
    lmList = detector.get_landmarks(img)

    state = recognizer.analyze(lmList)
    controller.update(state)

    if lmList:
        x, y = lmList[8][1], lmList[8][2]

        # 🔥 Neon cursor
        for i in range(3):
            cv2.circle(img, (x, y), 8 + i*3, (255, 0, 255), 1)

        cv2.circle(img, (x, y), 3, (0, 255, 255), -1)

    cv2.imshow("Gesture Control", img)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
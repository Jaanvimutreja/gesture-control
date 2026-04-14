import cv2
from hand_tracking import HandDetector
from gesture_logic import GestureRecognizer
from controls import Controller
import asyncio
import websockets
import json

current_gesture = "None"

# =========================
# 🔥 WEBSOCKET (optional)
# =========================
async def send_gesture(websocket):
    global current_gesture
    while True:
        data = {
            "gesture": current_gesture,
            "detected": current_gesture != "None"
        }
        await websocket.send(json.dumps(data))
        await asyncio.sleep(0.05)

# =========================
# 🔥 MAIN GESTURE LOOP
# =========================
async def gesture_loop():
    global current_gesture

    W, H = 1280, 720   # 🔥 bigger camera size

    cap = cv2.VideoCapture(0)
    cap.set(3, W)
    cap.set(4, H)

    detector = HandDetector()
    recognizer = GestureRecognizer()
    controller = Controller(W, H)

    # 🔥 resizable window
    cv2.namedWindow("Gesture Control", cv2.WINDOW_NORMAL)
    cv2.resizeWindow("Gesture Control", 1200, 800)

    while True:
        success, img = cap.read()
        if not success:
            break

        img = cv2.flip(img, 1)

        # detect hand
        img = detector.find_hand(img)
        lmList = detector.get_landmarks(img)

        # analyze gesture
        state = recognizer.analyze(lmList)

        # apply control
        controller.update(state)

        # =========================
        # 🔥 DEBUG GESTURE STATE
        # =========================
        if lmList:
            if state.get("action") == "LEFT_CLICK":
                current_gesture = "CLICK"
            elif state.get("dragging"):
                current_gesture = "DRAG"
            elif state.get("action") == "VOLUME":
                current_gesture = "VOLUME"
            else:
                current_gesture = "MOVE"
        else:
            current_gesture = "None"

        # =========================
        # 🔥 CURSOR VISUAL
        # =========================
        if lmList:
            x, y = lmList[8][1], lmList[8][2]

            for i in range(3):
                cv2.circle(img, (x, y), 8 + i*3, (255, 0, 255), 1)

            cv2.circle(img, (x, y), 4, (0, 255, 255), -1)

        # =========================
        # 🔥 MODE DISPLAY
        # =========================
        

        cv2.putText(img, f"ACTION: {current_gesture}", (20, 90),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,0), 2)
        
        
        # show window
        cv2.imshow("Gesture Control", img)

        if cv2.waitKey(1) & 0xFF == 27:
            break

        await asyncio.sleep(0.01)

    cap.release()
    cv2.destroyAllWindows()

# =========================
# 🔥 MAIN
# =========================
async def main():
    server = await websockets.serve(send_gesture, "localhost", 8765)
    print("✅ WebSocket server started on ws://localhost:8765")

    await asyncio.gather(
        gesture_loop()
    )

if __name__ == "__main__":
    asyncio.run(main())
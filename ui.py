import cv2

class UI:
    def __init__(self):
        self.main_color = (255, 0, 255)   # neon purple
        self.accent_color = (255, 255, 0) # neon cyan

    # 🔥 Neon glow point
    def draw_glow_point(self, img, x, y):
        for i in range(3):
            cv2.circle(img, (x, y), 6 + i*3, self.main_color, 1)
        cv2.circle(img, (x, y), 3, self.accent_color, -1)

    # 🔥 Hand drawing (better)
    def draw_hand(self, img, lmList):
        if not lmList:
            return img

        # Draw key points only (reduce load)
        important_ids = [4, 8, 12, 16, 20]

        for lm in lmList:
            if lm[0] in important_ids:
                x, y = lm[1], lm[2]
                self.draw_glow_point(img, x, y)

        return img

    # 🔥 Top status bar
    def draw_status_bar(self, img, text):
        cv2.rectangle(img, (0, 0), (640, 50), (20, 20, 20), -1)
        cv2.putText(img, text, (20, 35),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, self.accent_color, 2)

    def render(self, img, state, hand_data):
        
        # Hand rendering
        if hand_data:
            lmList = hand_data.get("lmList", [])
            img = self.draw_hand(img, lmList)

        # Mode + Action text
        mode = state.get("mode", "MOUSE")
        action = state.get("action", "")

        status_text = f"{mode}"
        if action:
            status_text += f" | {action}"

        self.draw_status_bar(img, status_text)

        return img
import math
import time

def dist(p1, p2):
    return math.hypot(p2[0] - p1[0], p2[1] - p1[1])

class GestureRecognizer:
    def __init__(self):
        self.pinch_start = 0
        self.click_done = False
        self.dragging = False

    def analyze(self, lmList):
        state = {"mouse_pos": None, "action": None, "dragging": False}

        if not lmList:
            return state

        index = (lmList[8][1], lmList[8][2])
        thumb = (lmList[4][1], lmList[4][2])

        state["mouse_pos"] = index

        d = dist(index, thumb)
        now = time.time()

        # 🔥 CLICK + DRAG ONLY (CLEAN)
        if d < 40:
            if self.pinch_start == 0:
                self.pinch_start = now
                self.click_done = False

            duration = now - self.pinch_start

            # CLICK
            if duration < 0.2:
                if not self.click_done:
                    state["action"] = "LEFT_CLICK"
                    self.click_done = True

            # DRAG
            elif duration >= 0.3:
                self.dragging = True
                state["dragging"] = True

            return state

        # RESET
        self.pinch_start = 0
        self.dragging = False
        self.click_done = False

        return state
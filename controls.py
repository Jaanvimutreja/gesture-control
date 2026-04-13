import pyautogui
import numpy as np
import time

pyautogui.PAUSE = 0
pyautogui.FAILSAFE = False

class Controller:
    def __init__(self, cam_w, cam_h):
        self.screen_w, self.screen_h = pyautogui.size()
        self.cam_w = cam_w
        self.cam_h = cam_h

        self.margin = 80

        self.prev_x = 0
        self.prev_y = 0
        self.alpha = 0.2

        self.is_dragging = False
        self.last_click = 0

    def update(self, state):
        pos = state.get("mouse_pos")
        action = state.get("action")
        dragging = state.get("dragging", False)

        if not pos:
            return

        cam_x, cam_y = pos

        # mapping
        screen_x = np.interp(cam_x, (self.margin, self.cam_w - self.margin), (0, self.screen_w))
        screen_y = np.interp(cam_y, (self.margin, self.cam_h - self.margin), (0, self.screen_h))

        # clamp
        screen_x = max(0, min(self.screen_w, screen_x))
        screen_y = max(0, min(self.screen_h, screen_y))

        # smoothing
        smooth_x = self.alpha * screen_x + (1 - self.alpha) * self.prev_x
        smooth_y = self.alpha * screen_y + (1 - self.alpha) * self.prev_y

        self.prev_x = smooth_x
        self.prev_y = smooth_y

        pyautogui.moveTo(int(smooth_x), int(smooth_y))

        # 🔥 DRAG LOGIC
        if dragging and not self.is_dragging:
            pyautogui.mouseDown()
            self.is_dragging = True

        elif not dragging and self.is_dragging:
            pyautogui.mouseUp()
            self.is_dragging = False

        # 🔥 CLICK LOGIC
        if action == "LEFT_CLICK" and not self.is_dragging:
            if time.time() - self.last_click > 0.3:
                pyautogui.click()
                self.last_click = time.time()
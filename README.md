# 🖐️ Gesture Control System

Control your laptop using hand gestures in real-time using just your webcam.

---

## 🚀 Overview

This project allows you to move your cursor, click, and drag using hand gestures detected via your webcam. It is designed to feel as natural as using a real mouse.

---

## ✨ Features

* 🖱️ Cursor movement using hand tracking
* 👆 Pinch gesture for left click
* ✊ Hold pinch for drag & drop
* 🎯 Click freeze for accurate selection
* ⚡ Smooth and responsive cursor
* 💫 Neon cursor visualization

---

## 🧠 Tech Stack

* Python
* OpenCV
* MediaPipe
* PyAutoGUI
* NumPy

---

## ⚙️ Installation

```bash
pip install opencv-python mediapipe pyautogui numpy
```

---

## ▶️ Run the Project

```bash
python main.py
```

---

## 🎮 Controls

| Gesture               | Action      |
| --------------------- | ----------- |
| Move hand             | Move cursor |
| Pinch (thumb + index) | Left click  |
| Hold pinch            | Drag        |

---

## ⚙️ How It Works

1. Webcam captures your hand in real-time
2. MediaPipe detects hand landmarks
3. Gesture logic identifies pinch gestures
4. Cursor movement is mapped to screen coordinates
5. PyAutoGUI executes mouse actions

---

## ⚡ Challenges Solved

* Cursor jitter → solved with smoothing
* Wrong clicks → fixed using click freeze
* Tracking instability → optimized detection
* Lag issues → reduced processing overhead

---

## 🚀 Future Improvements

* Right click gesture
* Scroll control using hand
* Multi-hand support
* Custom gesture mapping
* UI dashboard

---

## 👩‍💻 Author

Developed as a real-time gesture-based interaction system focusing on usability and performance.

---

## ⭐ Support

If you like this project, consider giving it a ⭐ on GitHub!

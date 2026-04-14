# 🖐️ Gesture Control System

A real-time gesture-based computer control system built using Python, OpenCV, and MediaPipe.  
This project enables users to control the mouse using hand gestures without touching any physical device.

---

## 🚀 Features

- 🖱️ Cursor movement using hand tracking
- 🤏 Click using pinch gesture (thumb + index)
- ✊ Drag using hold gesture
- 🎯 Smooth and stable cursor control (with filtering)
- ⚡ Real-time performance using OpenCV
- 🔌 WebSocket integration for real-time gesture streaming

---

## 🧠 How It Works

1. Camera captures real-time video
2. Hand is detected using MediaPipe
3. Landmarks (21 points) are extracted
4. Gesture logic interprets finger positions
5. Controller maps gestures to system actions
6. WebSocket streams gesture data in real-time

---

## ⚙️ Tech Stack

- Python  
- OpenCV  
- MediaPipe  
- PyAutoGUI  
- WebSockets  
- NumPy  

---

## 📦 Installation

```bash
pip install opencv-python mediapipe pyautogui numpy websockets
```

---

## ▶️ Run the Project

```bash
python main.py
```

---

## 🎮 Controls

| Gesture | Action |
|--------|--------|
| Move index finger | Move cursor |
| Pinch (short) | Left click |
| Hold pinch | Drag |

---

## 🏗️ Project Structure

```
gesture-control/
│
├── main.py              # Main execution loop
├── hand_tracking.py    # Hand detection using MediaPipe
├── gesture_logic.py    # Gesture recognition logic
├── controls.py         # System control (mouse actions)
├── utils.py            # Helper functions
└── ui.py               # UI overlays
```

---

## 🔌 WebSocket Integration

- Runs on: `ws://localhost:8765`
- Streams gesture data in real-time
- Can be connected to a frontend dashboard

---


## 💡 Future Improvements

- Scroll gesture  
- Volume & brightness control  
- Multi-hand detection  
- Frontend UI dashboard  
- Gesture customization  

---

## 👩‍💻 Author

**Jaanvi Mutreja**

---

⭐ If you like this project, give it a star!

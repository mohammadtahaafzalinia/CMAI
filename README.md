# Smart Mouse – Gesture-Controlled Virtual Mouse Using Image Processing

## Overview

Smart Mouse is a computer vision project that replaces the physical mouse with hand gestures. Using a standard webcam, the system tracks the user's hand in real time and translates finger movements into cursor actions. No extra hardware is needed, which makes it a low-cost, touch-free way to interact with a computer.

## How It Works

1. **Video capture:** The webcam streams live frames, which are flipped horizontally so movement feels natural.
2. **Hand detection and tracking:** Each frame is processed to locate the hand and extract key landmarks, such as fingertips and joints, using OpenCV and a hand-tracking model (e.g., MediaPipe).
3. **Gesture recognition:** The system checks which fingers are raised and measures the distances between landmarks to identify the current gesture.
4. **Cursor control:** The position of the index finger is mapped from the camera frame to the screen resolution. Smoothing is applied to reduce jitter and keep the pointer stable.
5. **Action execution:** Recognized gestures trigger mouse events (move, click, double-click, right-click, scroll, drag) through an automation library such as PyAutoGUI.

## Supported Gestures

| Action | Gesture |
| --- | --- |
| Move cursor | Index finger raised |
| Left click | Index and middle fingers brought together |
| Right click | Thumb and index finger pinch |
| Scroll | Two fingers moving up or down |
| Drag and drop | Pinch and hold, then move |

## Key Features

- Real-time performance with low latency
- Touch-free, hardware-free interaction using only a webcam
- Smooth cursor movement through coordinate interpolation
- Configurable gestures and sensitivity
- Useful for accessibility, presentations, and hygienic public interfaces

## Technologies Used

- **Language:** Python
- **Libraries:** OpenCV, MediaPipe, NumPy, PyAutoGUI

## Installation

```bash
git clone https://github.com/<your-username>/smart-mouse.git
cd smart-mouse
python -m venv venv
source venv/bin/activate        # On Windows: venv\Scripts\activate
pip install opencv-python mediapipe numpy pyautogui
```

## Usage

```bash
python main.py
```

- Make sure your webcam is connected and the hand is clearly visible in good lighting.
- Press `q` in the preview window to quit.

## Applications

- Assistive technology for people with limited mobility
- Hands-free control during presentations or lectures
- Touchless kiosks and public displays
- Human-computer interaction research

## Future Improvements

- Support for more custom gestures
- Better performance in low-light conditions
- Multi-hand support
- Machine-learning-based gesture classification for higher accuracy

## License

This project is licensed under the MIT License.

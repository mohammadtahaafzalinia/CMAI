# CMAI – Gesture-Controlled Virtual Mouse Using Image Processing

## Overview

CMAI is a computer vision project that replaces the physical mouse with hand gestures. Using a standard webcam, the system tracks the user's hand in real time and translates finger movements into cursor actions. No extra hardware is needed, which makes it a low-cost, touch-free way to interact with a computer.

## How It Works

1. **Video capture:** OpenCV reads live webcam frames at 640×480 and 30 FPS. Each frame is flipped horizontally so the cursor moves in the same direction as the hand.
2. **Hand detection and tracking:** Each frame is converted to RGB and passed to MediaPipe Hands (one hand, lightweight model, 0.6 detection and tracking confidence) to extract 21 hand landmarks.
3. **Cursor control:** The index fingertip position is scaled to the screen resolution. Exponential smoothing (factor `alpha = 0.25`) reduces jitter and keeps the pointer stable.
4. **Gesture recognition:** The normalized distances between the thumb tip and the index and middle fingertips are measured on every frame.
5. **Action execution:** When a distance falls below its threshold, PyAutoGUI triggers a mouse click. A click state flag ensures one click per pinch; the fingers must separate before the next click.

## Supported Gestures

| Action | Gesture | Threshold |
| --- | --- | --- |
| Move cursor | Move the index fingertip | – |
| Left click | Pinch thumb and index finger together | distance < 0.06 |
| Right click | Pinch thumb and middle finger together | distance < 0.05 |

## Key Features

- Real-time performance with low latency (lightweight MediaPipe model)
- Touch-free, hardware-free interaction using only a webcam
- Smooth cursor movement through exponential smoothing
- Single-click-per-pinch logic to prevent repeated accidental clicks
- Adjustable sensitivity through simple parameters (`alpha` and the click thresholds)
- Preview window with live camera feed; press `q` to quit

## Technologies Used

- **Language:** Python
- **Libraries:** OpenCV, MediaPipe, PyAutoGUI

## Applications

- Assistive technology for people with limited mobility
- Hands-free control during presentations or lectures
- Touchless kiosks and public displays
- Human-computer interaction research

## Future Improvements

- Scroll and drag-and-drop gestures
- Double-click support
- Mapping a smaller active area of the camera frame to the full screen for easier reach to the edges
- Hand landmarks drawn on the preview window
- Better performance in low-light conditions
- Multi-hand support
- Machine-learning-based gesture classification for higher accuracy

## License

This project is licensed under the MIT License.

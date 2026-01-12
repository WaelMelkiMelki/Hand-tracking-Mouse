# 🖐️ Hand Gesture Control

A real-time dual-hand gesture recognition system that allows you to control your computer using hand gestures captured via webcam. Built with Python, OpenCV, and MediaPipe.

## ✨ Features

- **Real-time Hand Tracking** - Detects and tracks up to 2 hands simultaneously
- **Gesture Recognition** - Recognizes multiple dual-hand gestures
- **Map/Screen Control** - Control zoom, pan, and rotation with intuitive gestures

### Supported Gestures

| Gesture | Action | Description |
|---------|--------|-------------|
| 🔍 **Zoom In** | Spread hands apart | Move hands away from each other |
| 🔎 **Zoom Out** | Bring hands together | Move hands closer to each other |
| ↩️ **Rotate Left** | Left hand higher | Position left palm above right palm |
| ✋ **Pan** | Right hand higher | Move cursor to right palm position |
| 🎮 **Steering Wheel** | Tilt hands | Rotate like steering a wheel |

## 📋 Requirements

- Python 3.7+
- Webcam

## 🚀 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/hand_gesture_control.git
   cd hand_gesture_control
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

## 📦 Dependencies

- `opencv-python` - Image processing and webcam capture
- `mediapipe` - Hand detection and landmark tracking
- `pyautogui` - System control (mouse, keyboard, scroll)
- `numpy` - Numerical operations

## 🎮 Usage

Run the main script:

```bash
python main.py
```

- Position both hands in front of the webcam
- Perform gestures to control your screen
- Press `Q` to quit the application

## 📁 Project Structure

```
hand_gesture_control/
├── main.py                 # Entry point - webcam capture and main loop
├── hand_tracker.py         # HandTracker class using MediaPipe
├── gesture_recognition.py  # Gesture detection logic
├── actions.py              # MapController for executing actions
├── requirements.txt        # Python dependencies
└── README.md              # This file
```

## 🔧 How It Works

1. **Hand Tracking** (`hand_tracker.py`) - Uses MediaPipe to detect hands and extract 21 landmark points per hand
2. **Gesture Recognition** (`gesture_recognition.py`) - Analyzes the relative positions and distances between hands to identify gestures
3. **Action Execution** (`actions.py`) - Translates recognized gestures into system actions using PyAutoGUI

## ⚙️ Configuration

You can adjust detection sensitivity in `hand_tracker.py`:

```python
HandTracker(
    mode=False,              # False for video stream
    max_hands=2,             # Maximum hands to detect
    detection_confidence=0.5, # Detection threshold (0-1)
    tracking_confidence=0.5   # Tracking threshold (0-1)
)
```

## 🤝 Contributing

Contributions are welcome! Feel free to:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 🙏 Acknowledgments

- [MediaPipe](https://mediapipe.dev/) - Google's ML framework for hand tracking
- [OpenCV](https://opencv.org/) - Computer vision library
- [PyAutoGUI](https://pyautogui.readthedocs.io/) - Cross-platform GUI automation
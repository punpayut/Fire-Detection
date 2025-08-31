# Fire Detection

A lightweight real-time video analytics project that detects fire and smoke in video streams using Ultralytics YOLO and Telegram alerts. The project demonstrates end-to-end object detection, live visualization, and alerting when fires or smoke are detected for the first time.

[![GitHub stars](https://img.shields.io/github/stars/punpayut/Fire-Detection?style=flat-square)](https://github.com/punpayut/Fire-Detection)
[![Open Issues](https://img.shields.io/github/issues/punpayut/Fire-Detection?style=flat-square)](https://github.com/punpayut/Fire-Detection/issues)
[![Pull Requests](https://img.shields.io/github/issues-pr/punpayut/Fire-Detection?style=flat-square)](https://github.com/punpayut/Fire-Detection/pulls)
[![License](https://img.shields.io/github/license/punpayut/Fire-Detection?style=flat-square)](LICENSE)

Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Technologies](#technologies)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)

## Installation

Prerequisites:
- Python 3.8+
- Git

1. Clone the repository
   - git clone https://github.com/punpayut/Fire-Detection.git
   - cd Fire-Detection

2. Create a virtual environment (optional but recommended)
   - Windows:
     - python -m venv venv
     - venv\\Scripts\\activate
   - macOS/Linux:
     - python3 -m venv venv
     - source venv/bin/activate

3. Install dependencies
   - pip install ultralytics cvzone opencv-python python-dotenv requests

4. Prepare environment variables
   - Copy env_sample to .env and populate BOT_TOKEN and CHAT_ID
   - cp env_sample .env  (or manually edit .env)
   - Note: env_sample contains a template for Telegram bot credentials

5. Ensure model and media are available
   - The repository includes best11.pt (weights) and sample video files (fire.mp4, small_fire.mp4, smoke.mp4)
   - Place any required video file referenced by the script in the repository root or adjust the script to point to your video source

6. Run the main script
   - python fire-detection.py

Notes:
- The script reads environment variables via dotenv and uses Telegram to send alerts the first time a fire or smoke is detected.
- To switch input sources from a video file to a webcam, edit the line that initializes the video capture:
  - cap = cv2.VideoCapture(0)  # Use default webcam
  - Or provide a path to another video file.

## Usage

The script processes a video stream, runs YOLO-based detection on each frame, and draws bounding boxes with class labels and confidence. Alerts are sent to Telegram when a fire or smoke is detected for the first time.

Example snippet (from fire-detection.py):
```python
cap = cv2.VideoCapture('fire.mp4')
model = YOLO('best11.pt')
# ... main loop with detection, drawing, and Telegram alerting ...
```

To run with a webcam:
```python
cap = cv2.VideoCapture(0)
```

To customize the Telegram alert behavior, modify the alert flags and the send_alert(...) function in fire-detection.py.

## Features

- Real-time detection of fire, smoke, and other in-frame objects using a YOLOv11 model
- Visual overlays: bounding boxes and class labels with confidence
- Telegram-based alerting for the first fire/smoke detection
- Adjustable frame rate handling for smoother playback
- Simple, self-contained script with a minimal set of dependencies

## Technologies

- Python
- Ultralytics YOLO (YOLOv11)
- OpenCV (cv2)
- cvzone (text overlays)
- python-dotenv (environment variables)
- requests (HTTP requests to Telegram Bot API)

## Project Structure

- .gitattributes
- best11.pt                 # Pre-trained YOLOv11 weights
- env_sample                 # Template for environment variables (.env)
- fire-detection.py            # Main detection and alerting script
- fire.mp4                     # Sample video input
- LICENSE
- small_fire.mp4
- smoke.mp4
- notebook/
  - notebook/Fire_detection_custom_dataset_YOLOV11.ipynb

Notes:
- The core logic resides in fire-detection.py, which loads the model, processes frames from a video source, draws detections, and sends alerts via Telegram.
- The env_sample file can be used as a starting point for setting BOT_TOKEN and CHAT_ID in a .env file.

## Contributing

Contributions are welcome. To contribute:
- Fork the repository
- Create a feature branch (e.g., feature/add-telegram-alerts)
- Implement changes and run locally
- Submit a pull request with a clear description of your changes

Guidelines:
- Follow the existing code style and ensure compatibility with Python 3.x
- Add tests or validation where feasible
- Update the README with any new usage instructions or dependencies

## License

MIT License

Copyright (c) 2025 Payut Charoensri

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

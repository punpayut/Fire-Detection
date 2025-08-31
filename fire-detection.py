from ultralytics import YOLO
import cvzone
import cv2
import math
import requests
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

# Running real-time from webcam
cap = cv2.VideoCapture('fire.mp4')
model = YOLO('best11.pt')

# Reading the classes
classnames = ['fire', 'other', 'smoke']
colors = [(0, 0, 255), (0, 255, 0), (255, 0, 0)]  # Red for 'fire', Green for 'other', Blue for 'smoke'

fire_alert_sent = False  # Flag for fire alert
smoke_alert_sent = False  # Flag for smoke alert

# Adjust frame rate
desired_fps = 60
delay = int(1000 / desired_fps)  # Convert FPS to milliseconds

def send_alert(detected_class, frame):
    """Send an alert with an image when fire or smoke is detected for the first time."""
    filename = f"{detected_class}_detected.jpg"
    cv2.imwrite(filename, frame)  # Save frame

    # Send image to Telegram
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendPhoto"
    try:
        with open(filename, "rb") as photo:
            response = requests.post(url, data={"chat_id": CHAT_ID, "caption": f"🔥 {detected_class.upper()} detected!"}, files={"photo": photo})
            if response.status_code == 200:
                print(f"{detected_class.capitalize()} alert sent to Telegram!")
    except Exception as e:
        print(f"Failed to send {detected_class} alert: {e}")

while True:
    ret, frame = cap.read()
    if not ret:
        break  # Stop if no frame is returned

    frame = cv2.resize(frame, (640, 480))
    result = model(frame, stream=True)

    for info in result:
        boxes = info.boxes
        for box in boxes:
            confidence = box.conf[0]
            confidence = math.ceil(confidence * 100)
            Class = int(box.cls[0])

            if confidence > 50:
                x1, y1, x2, y2 = box.xyxy[0]
                x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
                color = colors[Class]
                cv2.rectangle(frame, (x1, y1), (x2, y2), color, 2)
                cvzone.putTextRect(frame, f'{classnames[Class]} {confidence}%', [x1 + 8, y1 + 100],
                                   scale=1.5, thickness=1, colorB=color)

                detected_class = classnames[Class]

                # Send alert for the first smoke if no fire detected
                if detected_class == 'smoke' and not smoke_alert_sent and not fire_alert_sent:
                    smoke_alert_sent = True
                    send_alert(detected_class, frame)

                # Send alert for the first fire
                if detected_class == 'fire' and not fire_alert_sent:
                    fire_alert_sent = True
                    send_alert(detected_class, frame)

    # Display the frame with rectangles
    cv2.imshow('frame', frame)
    
    # Control FPS (60 FPS)
    if cv2.waitKey(delay) & 0xFF == ord('q'):  # Press 'q' to exit
        break

# Release resources
cap.release()
cv2.destroyAllWindows()

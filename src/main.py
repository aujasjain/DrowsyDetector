import os
import sys
import cv2

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.config import EAR_THRESHOLD, FRAME_THRESHOLD
from src.eye_tracker import detect_drowsiness
from src.alarm import play_alarm, stop_alarm  

counter = 0
alarm_on = False

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    _, ear = detect_drowsiness(frame, gray)

    if ear is not None and ear < EAR_THRESHOLD:
        counter += 1

        if counter >= FRAME_THRESHOLD:
            if not alarm_on:
                alarm_on = True
                play_alarm()
    else:
        if alarm_on:
            stop_alarm()
            alarm_on = False
        counter = 0

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()

import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ALARM_SOUND = os.path.abspath(os.path.join(BASE_DIR, "../data/alarm.mp3"))

SHAPE_PREDICTOR_PATH = "data/shape_predictor_68_face_landmarks.dat"

EAR_THRESHOLD = 0.25 
FRAME_THRESHOLD = 20  


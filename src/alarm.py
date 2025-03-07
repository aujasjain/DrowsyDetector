import pygame
import os
import time
from src.config import ALARM_SOUND

pygame.mixer.init()

def play_alarm():
    """Start playing the alarm if it's not already playing."""
    if not pygame.mixer.music.get_busy():  
        pygame.mixer.music.load(ALARM_SOUND)
        pygame.mixer.music.play(-1)  
        print("🚨 ALARM STARTED 🚨")

def stop_alarm():
    """Stop the alarm if it's playing."""
    if pygame.mixer.music.get_busy(): 
        pygame.mixer.music.stop()
        print("✅ ALARM STOPPED ✅")

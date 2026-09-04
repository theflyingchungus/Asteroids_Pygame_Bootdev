import os
import sys

import pygame

shoot_sound = None
break_sound = None


def get_asset_path(relative_path):
    if hasattr(sys, "_MEIPASS"):
        return os.path.join(sys._MEIPASS, relative_path)

    base_path = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(base_path, relative_path)


def init_sounds():
    global shoot_sound, break_sound
    shoot_sound = pygame.mixer.Sound(get_asset_path("laser.mp3"))
    break_sound = pygame.mixer.Sound(get_asset_path("snare.mp3"))

    # Optional: adjust volume (from 0.0 to 1.0)
    shoot_sound.set_volume(0.5)
    break_sound.set_volume(0.7)

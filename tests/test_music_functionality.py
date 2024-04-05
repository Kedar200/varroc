import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
import unittest
import subprocess


class TestMusic(unittest.TestCase):
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)

    def setUp(self):
        pass
    
    def test_start_music(self):
        adb_command = "adb shell input keyevent KEYCODE_MEDIA_PLAY_PAUSE"
        try:
            subprocess.run(adb_command, shell=True, check=True)
            print("Spotify playback toggled successfully.")
        except subprocess.CalledProcessError as e:
            print(f"Error: {e}")

    def test_stop_music(self):
        adb_command = "adb shell input keyevent KEYCODE_MEDIA_PLAY_PAUSE"

        try:
            subprocess.run(adb_command, shell=True, check=True)
            print("Music playback stopped successfully.")
        except subprocess.CalledProcessError as e:
            print(f"Error: {e}")

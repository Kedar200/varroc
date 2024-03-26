import sys
import os
import cv2
import numpy as np
# Add the parent directory to the sys.path
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from utils.adb_utils import ADBUtils

class ScreenProjection:
    def __init__(self):
        # Initialize any necessary parameters or resources
        pass

    def start_screen_mirroring(self):
        # Start screen mirroring from mobile device to PC/laptop
        adb_utils = ADBUtils()
        adb_utils.connect_to_device()
        
        # Start screen mirroring from mobile device to PC/laptop
        while True:
            image_bytes = adb_utils.device.screencap()
            if len(image_bytes)>0:
                frame = cv2.imdecode(np.frombuffer(image_bytes, dtype=np.uint8), cv2.IMREAD_COLOR)
                cv2.imshow("Screen Mirroring", frame)
                cv2.waitKey(1)
    def capture_screen(self):
        # Capture the screen from PC/laptop
        print("Capturing screen")
        # Placeholder for capturing the screen using appropriate library or tool
        captured_screen = None
        return captured_screen

if __name__ == "__main__":
    screen_projection = ScreenProjection()
    screen_projection.start_screen_mirroring()
    captured_screen = screen_projection.capture_screen()
    print("Captured screen:", captured_screen)

import sys
import os
# Add the parent directory to the sys.path
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from utils.adb_utils import ADBUtils


class MobileController:
    def __init__(self):
        # Initialize any necessary parameters or resources
        self.adb_utils = ADBUtils()
        self.adb_utils.connect_to_device()


    def tap_on_element(self,x,y):

        self.adb_utils.device.shell(f"input tap {x} {y}")


    def swipe(self,x1,y1,x2,y2,time):
        # Simulate scrolling down on the mobile device
        self.adb_utils.device.shell(f"input swipe {x1} {y1} {x2} {y2} {time}")



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


    def tap_on_element(self):

        self.adb_utils.device.shell(f"input tap 800 400")


    def scroll_down(self):
        # Simulate scrolling down on the mobile device
        self.adb_utils.device.shell(f"input swipe 500 500 500 100 100")



if __name__ == "__main__":
    # Example usage
    mobile_controller = MobileController()
    # mobile_controller.tap_on_element()
    mobile_controller.scroll_down()

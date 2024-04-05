import unittest
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from scripts.screen_projection import ScreenProjection
from utils import adb_utils


class TestScreenMirroring(unittest.TestCase):
    def __init__(self, methodName: str = "runTest") -> None:
        usbconnection=adb_utils.ADBUtils()
        usbconnection.connect_to_device()
        self.device=usbconnection.device
        super().__init__(methodName)

    def setUp(self):
        self.screen_projection= ScreenProjection(self.device)


    def test_capture_screen(self):
        captured_screen = self.device.screencap()
        self.assertIsNotNone(captured_screen)  

if __name__ == "__main__":
    unittest.main()

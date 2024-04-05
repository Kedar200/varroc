import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from scripts.mobile_control import MobileController
import unittest


# mobile_controller.tap_on_element(500,500)


class TestControl(unittest.TestCase):
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
    def setUp(self):
        self.mobile_controller = MobileController()
    
    def test_swipe(self):
        self.mobile_controller.swipe(100,900,100,200,100)
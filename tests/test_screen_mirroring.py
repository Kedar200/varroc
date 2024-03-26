import unittest
from unittest.mock import MagicMock

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from scripts.screen_projection import ScreenProjection

class TestScreenMirroring(unittest.TestCase):
    def setUp(self):
        # Mocking ScreenProjection class for testing
        self.screen_projection = ScreenProjection()
        self.screen_projection.adb_utils = MagicMock()
        self.screen_projection.adb_utils.device.screencap.return_value = b'fake_image_bytes'

    def test_start_screen_mirroring(self):
        self.screen_projection.start_screen_mirroring()
        self.assertTrue(self.screen_projection.adb_utils.connect_to_device.called)
        self.assertTrue(self.screen_projection.adb_utils.device.screencap.called)

    def test_capture_screen(self):
        captured_screen = self.screen_projection.capture_screen()
        self.assertIsNotNone(captured_screen)  # Placeholder for actual implementation

if __name__ == "__main__":
    unittest.main()

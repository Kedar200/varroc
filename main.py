from tests import test_music_functionality
from tests import test_navigation
from tests import test_screen_mirroring
from scripts import screen_projection
from utils import adb_utils


usbconnection=adb_utils.ADBUtils()

usbconnection.connect_to_device()

screen= screen_projection.ScreenProjection(usbconnection.device)
screen.start_screen_mirroring()

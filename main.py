import time
import multiprocessing
from tests import test_music_functionality
from tests import test_navigation
from tests import test_screen_mirroring
from scripts import screen_projection
from utils import adb_utils
from unittest import TestLoader, TestSuite, TextTestRunner

# Function to start screen mirroring
def start_screen_mirroring():
    usbconnection = adb_utils.ADBUtils()
    usbconnection.connect_to_device()
    screen = screen_projection.ScreenProjection(usbconnection.device)
    screen.start_screen_mirroring()
    # Add a loop to 
    # keep the screen mirroring process running until terminated
    while True:
        pass

# Function to run tests
def run_tests():
    # Load test cases
    screen_test = TestLoader().loadTestsFromTestCase(test_screen_mirroring.TestScreenMirroring)
    screen_navigation = TestLoader().loadTestsFromTestCase(test_navigation.TestControl)
    play_music = TestLoader().loadTestsFromTestCase(test_music_functionality.TestMusic)
    
    # Create test suites
    suite1 = TestSuite(screen_test)
    suite2 = TestSuite(screen_navigation)
    suite3 = TestSuite(play_music)
    
    # Run tests
    runner = TextTestRunner()
    runner.run(suite1)
    
    # Add a delay after running the first test suite
    time.sleep(5)  # Add a delay of 5 seconds
    
    runner.run(suite2)
    
    # Add a delay after running the second test suite
    time.sleep(5)  # Add a delay of 5 seconds
    
    runner.run(suite3)

if __name__ == "__main__":
    # Start screen mirroring process
    screen_process = multiprocessing.Process(target=start_screen_mirroring)
    screen_process.start()
    
    # Run tests in a separate process
    run_tests()
    
    # Terminate the screen mirroring process after tests are done
    screen_process.terminate()

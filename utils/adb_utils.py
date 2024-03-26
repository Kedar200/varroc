from ppadb.client import Client as AdbClient

class ADBUtils:
    def __init__(self):
        # Initialize any necessary parameters or 
        self.client = AdbClient(host="127.0.0.1", port=5037)

    def connect_to_device(self):
        # Connect to the mobile device using ADB over USB
        self.devices = self.client.devices()

        if len(self.devices) == 0:
            print("No devices attached")
            exit()
        self.device = self.devices[0]


    def disconnect_device(self):
        # Disconnect the mobile device
        print("Disconnected")
        pass

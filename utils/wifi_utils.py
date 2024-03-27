from ppadb.client import Client as AdbClient

class WiFiUtils:
    def __init__(self):
        pass

    def connect_to_device_over_wifi(self, ip_address):
        # Connect to the device over Wi-Fi using the specified IP address
        wifi_client = AdbClient(host="192.168.29.121", port=5555)
        wifi_devices = wifi_client.devices()

    def disconnect_from_device_over_wifi(self):
        # Disconnect from the device connected over Wi-Fi
        pass
if __name__ == "__main__":
    wifi_utils = WiFiUtils()
    ip_address = "127.0.0.1"  # Replace with your device's IP address
    wifi_utils.connect_to_device_over_wifi(ip_address)

# Cluster Automation Testing

This project aims to automate testing for features like Screen Mirroring, Navigation, Music, and Call functionality on a mobile device. The mobile screen is projected on a PC/laptop, allowing for control and backend image processing using Python.

## Overview

The automation testing framework consists of several components:

1. **Scripts**: Python scripts for controlling the mobile device, projecting the screen on the PC, and backend processing of captured images.
2. **Tests**: Test scripts written using the `unittest` framework to test different features such as screen mirroring, navigation, music functionality, and call functionality.
3. **Utils**: Utility scripts for common tasks like interacting with ADB, managing Wi-Fi connections, and image processing.

## Setup

1. Clone the repository to your local machine:

    ```bash
    git clone https://github.com/Kedar200/varroc.git
    ```

2. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Connect your mobile device to the PC/laptop via USB or Wi-Fi.

## Usage

1. Navigate to the `tests/` directory:

    ```bash
    cd tests/
    ```

2. Run the desired test script:

    ```bash
    python test_screen_mirroring.py
    ```

3. View the test results and any output generated during testing.

## Test Cases

### Screen Mirroring

- **Test 1**: Verify that the mobile screen is mirrored accurately on the PC/laptop.
- **Test 2**: Test user interaction on the mobile device and ensure it reflects correctly on the mirrored screen.
- **Test 3**: Validate screen mirroring performance under different network conditions (e.g., Wi-Fi vs. USB).

### Navigation

- **Test 1**: Test navigation through different screens and verify UI elements' visibility and functionality.
- **Test 2**: Verify smooth navigation transitions and responsiveness.

### Music Functionality

- **Test 1**: Test playback controls (play, pause, skip) and verify audio output.
- **Test 2**: Verify music playback behavior under various scenarios (e.g., incoming call interruption).

### Call Functionality

- **Test 1**: Test incoming call handling and verify screen behavior during an active call.
- **Test 2**: Test call initiation and verify call quality.

## Contributing

Contributions are welcome! If you'd like to contribute to this project, please fork the repository and submit a pull request with your changes.

This project is developed for the varroc Hackathon and is currently not licensed. All rights reserved.

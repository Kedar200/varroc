import sys
import os
import cv2
import numpy as np
from PySide6.QtGui import QImage, QPixmap
from PySide6.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

class ScreenProjection:
    def __init__(self,device):
        # Initialize any necessary parameters or resources
        self.device=device


    def start_screen_mirroring(self):
        app = QApplication(sys.argv)
        window = QWidget()
        layout = QVBoxLayout()
        label = QLabel()
        layout.addWidget(label)
        window.setLayout(layout)
        window.show()
        i=0
        while True:
            image_bytes = self.device.screencap()
            if len(image_bytes) > 0:
                frame = cv2.imdecode(np.frombuffer(image_bytes, dtype=np.uint8), cv2.IMREAD_COLOR)
                if frame is not None:
                    ratio = 50 / 200
                    image = QImage(frame, frame.shape[1], frame.shape[0], frame.shape[1] * 3, QImage.Format_BGR888)
                    pix = QPixmap(image)
                    pix.setDevicePixelRatio(1 / ratio)
                    label.setPixmap(pix)
            app.processEvents()
            i=i+1


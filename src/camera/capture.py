# src/camera/capture.py

import cv2


class Camera:
    def __init__(self, device=0):
        # Default camera is the first one
        self.device = device
        self.cap = cv2.VideoCapture(self.device)

    def open(self):
        if not self.cap.isOpened():
            self.cap.open(self.device)

    def capture_frame(self):
        if self.cap.isOpened():
            ret, frame = self.cap.read()
            if ret:
                return frame
            else:
                return None

    def close(self):
        if self.cap.isOpened():
            self.cap.release()

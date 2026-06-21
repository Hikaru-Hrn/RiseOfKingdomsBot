import cv2
import numpy as np
import mss
import pygetwindow as w
import time

class RoKScreenRecorder:
    def __init__(self, rok_window_title="Rise of Kingdoms", title="screen recorder", check_interval=0.5):
        self.window_title = rok_window_title
        self.title = title
        self.check_interval = check_interval

        self.last_check_time = time.time()
        self.mon = None

    def get_window(self):
        window = w.getWindowsWithTitle(self.window_title)
        if window:
            window = window[0]
        self.mon = {"top": window.top, "left": window.left, "width": window.width, "height": window.height}

    def screen_record(self):
        sct = mss.MSS()

        self.get_window()
        while True:
            current_time = time.time()
            if current_time - self.last_check_time > self.check_interval:
                self.last_check_time = current_time
                self.get_window()

            img = np.asarray(sct.grab(self.mon))

            cv2.imshow(self.title, img)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                cv2.destroyAllWindows()
                break


a = RoKScreenRecorder()
a.screen_record()

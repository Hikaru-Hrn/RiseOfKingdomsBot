import cv2
import numpy as np
import mss
import pygetwindow as w

def get_window():
    window = w.getWindowsWithTitle("Rise of Kingdoms")
    if window:
        window = window[0]
    return {"top": window.top, "left": window.left, "width":window.width, "height":window.height}


def screen_record():

    title = "screen recorder"
    sct = mss.MSS()

    while True:
        mon = get_window()
        img = np.asarray(sct.grab(mon))

        cv2.imshow(title, img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break

screen_record()

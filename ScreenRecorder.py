import cv2
import numpy as np
import mss


def screen_record():
    mon = {"top": 420, "left": 1320, "width": 800, "height": 600}

    title = "screen recorder"
    sct = mss.MSS()

    while True:
        img = np.asarray(sct.grab(mon))

        cv2.imshow(title, img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break

screen_record()
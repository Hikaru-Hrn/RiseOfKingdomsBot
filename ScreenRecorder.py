import cv2
import numpy as np
import pyscreenshot as ps

cv2.namedWindow('screenshot', cv2.WINDOW_GUI_EXPANDED)
while True:
    screenshot = ps.grab()
    frame = np.array(screenshot)
    frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
    cv2.imshow("screenshot", frame)

    key = cv2.waitKey(1)
    if key == ord('q'):
        break

    if key == ord('s'):
        cv2.imwrite("output.png", screenshot)

cv2.destroyAllWindows()
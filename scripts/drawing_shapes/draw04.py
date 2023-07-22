import numpy as np
import cv2

drawing = False
mode = True

ix, iy = -1, -1

def draw_circle(event, x, y, flags, param):
    global ix, iy, drawing, mode
    
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
    elif event == cv2.EVENT_MOUSEMOVE:  # Corrected event name
        if drawing == True:
            cv2.rectangle(img, (ix, iy), (x, y), (0, 255, 0), -1)
        else:
            cv2.circle(img, (x, y), 5, (0, 0, 255), -1)
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        if mode == True:
            cv2.rectangle(img, (ix, iy), (x, y), (0, 255, 0), -1)
        else:
            cv2.circle(img, (x, y), 5, (0, 0, 255), -1)

img = np.zeros((512, 512, 3), np.uint8)
cv2.namedWindow("img")
cv2.setMouseCallback("img", draw_circle)

while(1):
    cv2.imshow("img", img)  # Changed window name to match the namedWindow
    k = cv2.waitKey(1) & 0xFF
    if k == ord("m"):
        mode = not mode
    elif k == 27:
        break
cv2.destroyAllWindows()

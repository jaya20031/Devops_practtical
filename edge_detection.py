import cv2 as cv
import numpy as np

camera = cv.viedoCapture(0)
while True:
    _, frame = camera.read()
    laplacian = cv.Laplacian(frame, cv.CV_64F)
    laplacian = np.uint8(laplacian)
    cv.imshow("laplacian", laplacian)
    edges = cv.Canny(frame, 100, 100)
    cv.imshow("canny", edges)
    cv.imshow("camera", frame)
    if cv.waitkey(5) == ord("x"):
        break
camera.release()
cv.destroyAllwindows()

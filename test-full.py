import cv2
import numpy as np
import os
os.environ['SDL_VIDEO_CENTERED'] = '1'
vs = cv2.VideoCapture(0); #get input from webcam

while True:
    _,frame = vs.read();

    capname = "vs"
    cv2.namedWindow(capname, cv2.WND_PROP_FULLSCREEN)
    cv2.setWindowProperty(capname, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
    cv2.imshow(capname, frame)
#        cv2.waitKeyEx(40)
#	else:
#		break       
    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break
vs.release()
cv2.destroyAllWindows()
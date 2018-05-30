import numpy as np
import cv2
import datetime

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 320)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 240)
#cv2.VideoCapture.set(CV_CAP_PROP_FRAME_WIDTH, 640)
#cv2.VideoCapture.set(CV_CAP_PROP_FRAME_HEIGHT, 360)
#cap.SetCaptureProperty(CV_CAP_PROP_FRAME_WIDTH, 
#cap.set(cv2.CV_CAP_PROP_FRAME_WIDTH, 640);
#cap.set(cv2.CV_CAP_PROP_FRAME_HEIGHT, 360);

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    now = datetime.datetime.today().strftime('%Y%m%d_%H%M%S')
    print (now)
    # Display the resulting frame
    cv2.imshow('Mobile Legend Beng-beng',frame)
    #cv2.imshow('gray',gray)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
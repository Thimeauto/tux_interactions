import color_detector as cd
import params as p

color_detector = cd.Color_Detector()

color_detector.detect(p.DEFAULT_CAM_ID)

# import cv2
# import numpy as np

# cap = cv2.VideoCapture(0)

# while(True):
#     ret, frame = cap.read()

#     cv2.imshow('frame',frame)

#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
# cap.release()
# cv2.destroyAllWindows()
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 14 19:15:23 2022

@author: Ale
"""

import cv2
import mediapipe as mp
from edition import crop_face
mp_face_detection = mp.solutions.face_detection
mp_drawing = mp.solutions.drawing_utils

img_path = 'input/test.jpg'
out_path = 'output/'



# with mp_face_detection.FaceDetection(model_selection=0, min_detection_confidence=0.5) as face_detection:
with mp_face_detection.FaceDetection() as face_detection:
    image = cv2.imread(img_path)
    height, width, _ = image.shape
    image.flags.writeable = False
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = face_detection.process(image)
    # Draw the face detection annotations on the image.
    image.flags.writeable = True
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    if results.detections:
        for idx, detection in enumerate(results.detections):
            mp_drawing.draw_detection(image, detection)
            
            img_crop = crop_face(image, detection, height, width)
            img_name_out = out_path+str(idx)+'.jpg'
            cv2.imwrite(img_name_out, img_crop)

            
    cv2.imwrite(out_path+'detection.jpg', image)
    cv2.imshow('MediaPipe Face Detection', image)
    if cv2.waitKey(0) & 0xFF == 27:
        cv2.destroyAllWindows()

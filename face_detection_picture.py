# -*- coding: utf-8 -*-
"""
Created on Mon Mar 14 19:15:23 2022

@author: Ale
"""

import argparse
import cv2
import mediapipe as mp
from edition import crop_face
from utils import getBaseName

mp_face_detection = mp.solutions.face_detection
mp_drawing = mp.solutions.drawing_utils


parser = argparse.ArgumentParser()
parser.add_argument('-i', '--img_path', type=str, default='input/test1.jpg',
                    help='Please specify path for image', required=True)

parser.add_argument('-o', '--out_path', type=str, default='output/',
                    help='Please specify path for folder out', required=True)

opt = parser.parse_args()


with mp_face_detection.FaceDetection() as face_detection:
    image = cv2.imread(opt.img_path)
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

            img_crop = crop_face(image, detection)
            img_name_out = opt.out_path+getBaseName(opt.img_path)+str(idx)+'.jpg'
            cv2.imwrite(img_name_out, img_crop)

    cv2.imwrite(opt.out_path+getBaseName(opt.img_path)+'_detection.jpg', image)
    cv2.imshow('MediaPipe Face Detection', image)
    if cv2.waitKey(0) & 0xFF == 27:
        cv2.destroyAllWindows()

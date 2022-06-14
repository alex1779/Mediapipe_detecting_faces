# -*- coding: utf-8 -*-
"""
Created on Mon Mar 14 19:15:23 2022

@author: Ale
"""

import argparse
import cv2
import mediapipe as mp
from edition import draw_detection
from utils import getBaseName

# mp_drawing = mp.solutions.drawing_utils
# mp_drawing_styles = mp.solutions.drawing_styles
mp_face_mesh = mp.solutions.face_mesh


parser = argparse.ArgumentParser()
parser.add_argument('-i', '--img_path', type=str, default='data/example1.jpg',
                    help='Please specify path for image', required=True)

parser.add_argument('-o', '--out_path', type=str, default='output/',
                    help='Please specify path for folder out', required=True)


opt = parser.parse_args()

with mp_face_mesh.FaceMesh(static_image_mode=True, max_num_faces=20,
                           refine_landmarks=True, min_detection_confidence=0.5) as face_mesh:
    while True:
        image = cv2.imread(opt.img_path)
        # image = cv2.imread(opt.img_path)
        results = face_mesh.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
        # annotated_image = image.copy()
        for idx, face_landmarks in enumerate(results.multi_face_landmarks):

            draw_detection(image=image, face_landmarks=face_landmarks)

            img_crop = draw_detection(image, face_landmarks)
            img_name_out = opt.out_path+getBaseName(opt.img_path)+' '+str(idx)+'.jpg'
            cv2.imwrite(img_name_out, img_crop)
        
        cv2.imwrite(opt.out_path+getBaseName(opt.img_path)+'_detection.jpg', image)
        cv2.imshow('Face Detection Using Mesh', image)
        keypressed = cv2.waitKey(0)

        if keypressed == 27:
            cv2.destroyAllWindows()
            break

        if keypressed == ord('s'):
            print('Image Saved')
            saved = True

        if keypressed == ord('f'):
            fixEye = True

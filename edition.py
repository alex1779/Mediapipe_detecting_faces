# -*- coding: utf-8 -*-
"""
Created on Mon Jun 13 11:44:14 2022

@author: Ale
"""
import cv2


def crop_face(image, detection):
    height, width, _ = image.shape
    xmin = detection.location_data.relative_bounding_box.xmin
    ymin = detection.location_data.relative_bounding_box.ymin
    width_box = detection.location_data.relative_bounding_box.width
    height_box = detection.location_data.relative_bounding_box.height
    x1 = int(xmin*width)
    x2 = int(x1+width_box*width)
    y1 = int(ymin*height)
    y2 = int(y1+height_box*height)
    img_crop = image[y1:y2, x1:x2]

    return img_crop


def draw_detection(image, face_landmarks):
    height, width, _ = image.shape
    x, y = [], []
    for idx, landmark in enumerate(face_landmarks.landmark):
        x.append(landmark.x)
        y.append(landmark.y)
    x.sort()
    y.sort()
    
    xmin = x[0]
    ymin = y[0]
    width_box = x[-1]
    height_box = y[-1]

    x1 = int(xmin*width)
    x2 = int(width_box*width)
    y1 = int(ymin*height)
    y2 = int(height_box*height)
    rect_start_point = x1, y1
    rect_end_point = x2, y2
    color = (255, 255, 255)
    thickness = 2
    cv2.rectangle(image, rect_start_point, rect_end_point,
                  color, thickness)
    img_crop = image[y1:y2, x1:x2]

    return img_crop

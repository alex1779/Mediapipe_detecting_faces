# -*- coding: utf-8 -*-
"""
Created on Mon Jun 13 11:44:14 2022

@author: Ale
"""


def crop_face(image, detection, height, width):
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

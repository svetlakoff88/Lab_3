#!usr/bin/env python3
# -*- coding:utf-8 -*-

import cv2

img = 'scale_1200-8.png'


def img_prep(img_out, name):
    source = cv2.imread(img_out)  # read to pic
    thres, threshhold = cv2.threshold(source, 127, 255, 0)  # return pic with replaced pixels
    cv2.imshow(name, threshhold)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


img_prep(img, 'output')

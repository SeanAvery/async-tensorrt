import cv2
import random
import colorsys
from utils.coco_classes import COCO_CLASSES_LIST
import sys

class Visualizer():
    def __init__(self, color):
        # TODO: green gradient
        self.color = color
        self.color_list = self.gen_colors()
        print('self.color_list', self.color_list)
        print(len(self.color_list))

    def gen_colors(self):
        # generate random hues
        hsvs = []
        for x in range(len(COCO_CLASSES_LIST)):
            hsvs.append([float(x) / len(COCO_CLASSES_LIST), 1., 0.7])
        random.seed(13414)
        random.shuffle(hsvs)
        
        # convert hsv to rgb values
        rgbs = []
        for hsv in hsvs:
            (h, s, v) = hsv
            rgb = colorsys.hsv_to_rgb(h, s, v)
            rgbs.append(rgb)

        # convert to bgr and (0-255) range
        bgrs = []
        for rgb in rgbs:
            bgr = (int(rgb[2] * 255), int(rgb[1] * 255), int(rgb[0] * 255))
            bgrs.append(bgr)

        return bgrs

    def draw(self, frame, boxes, confs, clss):
        overlay = frame.copy()
        for bb, cf, cl in zip(boxes, confs, clss):
            x_min, y_min, x_max, y_max = bb[0], bb[1], bb[2], bb[3]
            print('cl', cl, COCO_CLASSES_LIST[cl])
            cls = COCO_CLASSES_LIST[cl]
            print('cf', cf)
            print('x_min', x_min)
            print('y_min', y_min)
            print('x_max', x_max)
            print('y_max', y_max)
            color = self.color_list[cl]
            print('color', color)
            cv2.rectangle(overlay, (x_min, y_min), (x_max, y_max), color, -1)
            cv2.putText(frame, cls, (x_min, y_min), fontFace=cv2.HERSHEY_SIMPLEX, fontSCale=2, color=(255, 255, 255))
        
        alpha = 0.4

        return cv2.addWeighted(overlay, alpha, frame, 1-alpha, 0)


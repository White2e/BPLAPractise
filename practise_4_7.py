# pip install ultralytics
import torch
import numpy as np
import pandas as pd
import cv2
import requests


class ObjectDetection:
    def __init__(self):
        self.__model = self.__load_model()
        self.classes = self.__model.names

        device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.__model.to(device)

    def __load_model(self):
        model = torch.hub.load('ultralytics/yolov5', 'yolov5x', pretrained=True)
        return model

    def detect_objects(self, image_path):
        img = cv2.imread(image_path)
        if img is None:
            return

        results = self.__model(img)

        detections = results.xyxy[0].cpu().numpy()

        for detection in detections:
            x1, y1, x2, y2, conf, class_id = detection
            cv2.rectangle(img, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 2)

        cv2.imshow('Detections', img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()


if __name__ == '__main__':
    obj = ObjectDetection()
    print(obj.classes)
    obj.detect_objects('img.jpg')

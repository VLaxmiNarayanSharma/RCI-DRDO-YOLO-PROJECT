from ultralytics import YOLO
import cv2
import matplotlib.pyplot as plt

model = YOLO("best.pt")
results = model("your_test_image.jpg")

results[0].show()

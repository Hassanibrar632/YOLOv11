import matplotlib.pyplot as plt
import numpy as np
import requests
import base64
import cv2

# Send image for inference
url = "http://localhost:5000/predict"
files = {"image": open("dataset/images/test/0_60_30_0_01614.jpg", "rb")}
response = requests.post(url, files=files)

response = response.json()

# Print detection results
print(response['message'], response['detections'])
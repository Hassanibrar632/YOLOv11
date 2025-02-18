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

org_image = response['orignal_image']
out_image = response['output_image']

image_data = base64.b64decode(org_image)
np_arr = np.frombuffer(image_data, np.uint8)
image = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)
plt.imsave("org.jpg", image)

image_data = base64.b64decode(out_image)
np_arr = np.frombuffer(image_data, np.uint8)
image = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)
plt.imsave("out.jpg", image)

# Print detection results
print(response['message'], response['detections'])
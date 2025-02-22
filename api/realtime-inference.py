import cv2
import requests
import base64
import numpy as np

# Server URL
url = "http://localhost:5000/predict"

# Initialize webcam
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("Error: Failed to capture image.")
        break
    
    # Encode frame as JPEG
    _, buffer = cv2.imencode(".jpg", frame)
    img_base64 = base64.b64encode(buffer).decode("utf-8")
    
    # Send frame for inference
    response = requests.post(url, files={"image": img_base64})
    response = response.json()
    
    # Draw bounding boxes on the image
    for detection in response['detections']:
        x1, y1, x2, y2 = detection['box']
        label = f"{detection['class']} ({detection['confidence']:.2f})"
        
        # Draw rectangle
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
        
        # Put label
        cv2.putText(frame, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
    
    cv2.imshow("Processed Image", frame)
    
    # Print detection results
    print(response['message'], response['detections'])
    
    # Exit on 'q' key
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Cleanup
cap.release()
cv2.destroyAllWindows()

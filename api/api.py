from flask import Flask, request, jsonify
from ultralytics import YOLO
import cv2
import numpy as np
from PIL import Image
import base64

app = Flask(__name__)

# Load the YOLO model (supports .pt or .onnx models)
model = YOLO("./models/best.onnx")  # Replace with your model path (yolov8.pt for PyTorch)

# Actual API to predtict using onix or pt
@app.route("/predict", methods=["POST"])
def predict():
    if "image" not in request.files:
        return jsonify({"error": "No image file provided"}), 400

    # Load image from request
    image_file = request.files["image"]
    image = np.frombuffer(image_file.read(), np.uint8)
    image = cv2.imdecode(image, cv2.IMREAD_COLOR)

    # Run YOLO inference
    results = model(image)

    # Extract predictions
    detections = []
    for result in results:
        for box, conf, cls in zip(result.boxes.xyxy.cpu().numpy(), 
                                  result.boxes.conf.cpu().numpy(), 
                                  result.boxes.cls.cpu().numpy()):
            detections.append({
                "class": model.names[int(cls)],
                "confidence": float(conf),
                "box": [int(box[0]), int(box[1]), int(box[2]), int(box[3])]
            })

    return jsonify({
        "message": "Inference completed successfully",      # Retrun Success Message
        "detections": detections,                           # Return Dtections
    }), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
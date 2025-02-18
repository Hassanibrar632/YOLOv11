from ultralytics import YOLO

# Load the YOLO model
model = YOLO("./tune/weights/best.pt")  # Replace with your model path

# Export the model to ONNX format
model.export(format="onnx")

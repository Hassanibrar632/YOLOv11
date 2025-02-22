# YOLOv11 Flask API

This directory contains a Flask-based API for running YOLOv11 inference on images. The API takes an image as input and returns detected objects along with a processed image containing bounding boxes.

## Files Overview
- **`api.py`**: The main API script that loads the YOLOv11 model and handles inference.
- **`test_api.py`**: A script to send test images to the API and visualize the results.
- **`models/`**: Directory where the YOLOv11 model (ONNX or PyTorch) is stored.

## Installation
To set up and run the API, follow these steps:

1. Install dependencies:
   ```bash
   pip install flask ultralytics opencv-python numpy pillow requests matplotlib
   ```

2. Ensure your model file is placed in the `models/` directory. Update the model path in `api.py` if necessary.

3. Run the Flask API:
   ```bash
   python api.py
   ```

## Usage
### Sending an Image for Inference
Once the API is running on `http://localhost:5000`, you can send an image for inference using `test_api.py`:
   ```bash
   python test_api.py
   ```

Alternatively, you can use `cURL`:
   ```bash
   curl -X POST -F "image=@path/to/your/image.jpg" http://localhost:5000/predict
   ```

### Expected API Response
The API returns a JSON response containing:
- `message`: Status of inference
- `detections`: List of detected objects with class, confidence, and bounding box

Example Response:
```json
{
    "message": "Inference completed successfully",
    "detections": [
        {"class": "car", "confidence": 0.95, "box": [30, 50, 200, 220]},
        {"class": "person", "confidence": 0.87, "box": [100, 150, 250, 400]}
    ]
}
```

## Realtime Inference:
The code uses this flask-api to infer the frames of webcam and give output from the api inference results. The code uses webcam to capture image then encodes that into byte form and send that to the api, upon getting the results the api then draws the detections based on the results and shows the frame.

## Notes
- The model is loaded in ONNX format by default (`models/best.onnx`). Modify `api.py` if using a `.pt` file.
- Ensure the API is running before testing with `test_api.py`.

## Acknowledgments
- **Ultralytics**: For the YOLOv11 model and documentation.
- **Flask**: For the web framework.
- **OpenCV & NumPy**: For image processing.


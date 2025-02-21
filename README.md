# YOLOv11 UAV Detection

This repository contains code and resources for fine-tuning YOLOv11n on the HIT-UAV dataset to achieve optimal hyperparameters for UAV-based detection of humans, cars, bikes, and other entities using AI.

## Table of Contents
- [Overview](#overview)
- [Installation](#installation)
- [Usage](#usage)
- [Training](#training)
- [Model Conversion](#model-conversion)
- [Folder Structure](#folder-structure)
- [License](#license)
- [Acknowledgments](#acknowledgments)

## Overview
The project leverages the latest YOLOv11n model from Ultralytics to enhance UAV-based object detection. By fine-tuning it on the HIT-UAV dataset, we aim to improve detection accuracy for various entities commonly found in aerial imagery.

## Installation
To set up the environment locally, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo-name.git
   cd your-repo-name
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
Once the dependencies are installed, you can use the available scripts for training and model conversion.

## Training
The training process is documented in `YOLOv11_Trainning.ipynb`. **This notebook was run on Google Colab, not locally.** If you wish to replicate the results:
1. Open `YOLOv11_Trainning.ipynb` in Google Colab.
2. Follow the provided instructions to load the dataset and train the model.

## Model Conversion
The `convert_pt2onix.py` script converts trained YOLOv11n models from PyTorch (`.pt`) to ONNX format using Ultralytics' export function. To convert a model:
   ```bash
   python convert_pt2onix.py --weights path/to/model.pt
   ```

## Folder Structure
This repository contains several key folders:

### `api/` - YOLOv11 Flask API
- Contains scripts for setting up a REST API using Flask.
- See [`api/README.md`](api/README.md) for setup and usage instructions.

### `dataset/` - Sample Dataset
- Contains example images, labels, and dataset configuration.
- **Important:** Modify `dataset.yaml` as instructed in `YOLOv11_Trainning.ipynb`.
- See [`dataset/README.md`](dataset/README.md) for more details.

### `training_results/` - Training Metrics & Outputs
- Stores training results, including hyperparameter tuning results, model weights, and evaluation metrics.
- Contains performance plots such as loss curves, confusion matrices, and validation results.
- See [`training_results/README.md`](training_results/README.md) for a detailed breakdown.

### `kaggle/` - Kaggle API Token Setup
- Contains instructions for setting up Kaggle API authentication.
- See [`kaggle/README.md`](kaggle/README.md) for guidance on using `kaggle.json`.

## License
This project is licensed under the MIT License.

## Acknowledgments
- **HIT-UAV Dataset**: Used for training. More details and author links are available in `YOLOv11_Trainning.ipynb` (data section).
- **Ultralytics**: For providing the YOLOv11 models and documentation.

---
For any issues or improvements, feel free to submit a pull request or open an issue!

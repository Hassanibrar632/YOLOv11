# YOLOv11 UAV Detection

This repository contains code and resources for fine-tuning YOLOv11n on the HIT-UAV dataset to achieve optimal hyperparameters for UAV-based detection of humans, cars, bikes, and other entities using AI. This can be really helpfull from military point-of-view.

## Table of Contents
- [Overview](#overview)
- [Installation](#installation)
- [Usage](#usage)
- [Training](#training)
- [Model Conversion](#model-conversion)
- [License](#license)
- [Acknowledgments](#acknowledgments)

## Overview
The project leverages the latest YOLOv11n model from Ultralytics to enhance UAV-based object detection. By fine-tuning it on the HIT-UAV dataset, we aim to improve detection accuracy for various entities commonly found in aerial imagery.

## Installation
To set up the environment locally, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/Hassanibrar632/YOLOv11.git
   cd YOLOv11
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
   > ### Warning:
   > Should use a virtual env using python-env or conda to avoid any unexpected installation or libraries conflits.
   > 
   > This code was ran on colab.
   > 
   > Must have kaggle key to download the dataset.
   > 
   > Instruction are also mention in detail in the `.ipynb` file. 

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

## License
This project is licensed under the MIT License.

## Acknowledgments
- **HIT-UAV Dataset**: Used for training. More details and author links are available in `YOLOv11_Trainning.ipynb` (data section).
- **Ultralytics**: For providing the YOLOv11 models and documentation.

---
For any issues or improvements, feel free to submit a pull request or open an issue!



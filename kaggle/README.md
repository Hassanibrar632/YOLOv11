# Kaggle Folder

This directory contains necessary files for running YOLOv11 training and inference on Kaggle.

## Files Overview
- **`past your token file here.txt`**: Placeholder file indicating where to place your Kaggle API token.

## Instructions
1. **Kaggle API Token**:
   - You need to download your Kaggle API token (`kaggle.json`).
   - Place the `kaggle.json` file inside this directory.
   - This file is required to access Kaggle datasets and notebooks programmatically.

2. **Setup Kaggle API**:
   - After placing the token file, run the following command to configure Kaggle:
     ```bash
     mkdir -p ~/.kaggle
     cp kaggle.json ~/.kaggle/
     chmod 600 ~/.kaggle/kaggle.json
     ```
   - This ensures that the Kaggle API can authenticate properly.

## Notes
- Do not share your `kaggle.json` file publicly, as it contains your credentials.
- This directory does not contain datasets; it is only for authentication purposes.


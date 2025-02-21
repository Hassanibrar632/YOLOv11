# YOLOv11 Training Results

This directory contains results from training and fine-tuning YOLOv11 on the HIT-UAV dataset. The results include performance metrics, visualizations, and weight files.

## Folder Overview

### `tune/`
Contains results from hyperparameter tuning.
- **`best_hyperparameters.yaml`**: Stores the optimal hyperparameters found during tuning.
- **`tune_fitness.png`**: ![Tune Fitness](/training_results/tune/tune_fitness.png)
- **`tune_results.csv`**: CSV file with tuning results.
- **`tune_scatter_plots.png`**: ![Tune Scatter Plots](/training_results/tune/tune_scatter_plots.png)
- **`weights/`**: Directory containing tuned model weight files.

### `best_fit/`
Contains results from the best-performing model.
- **`weights/`**: Directory with the best-trained model weights.
- **`F1_curve.png`**: ![F1 Curve](/training_results/best_fit/F1_curve.png)
- **`PR_curve.png`**: ![PR Curve](/training_results/best_fit/PR_curve.png)
- **`P_curve.png`**: ![Precision Curve](/training_results/best_fit/P_curve.png)
- **`R_curve.png`**: ![Recall Curve](/training_results/best_fit/R_curve.png)
- **`args.yaml`**: Training arguments used.
- **`confusion_matrix.png`**: ![Confusion Matrix](/training_results/best_fit/confusion_matrix.png)
- **`confusion_matrix_normalized.png`**: ![Normalized Confusion Matrix](/training_results/best_fit/confusion_matrix_normalized.png)
- **`labels.jpg`**: ![Label Distribution](/training_results/best_fit/labels.jpg)
- **`labels_correlogram.jpg`**: ![Label Correlogram](/training_results/best_fit/labels_correlogram.jpg)
- **`results.csv`**: Training results in CSV format.
- **`results.png`**: ![Results Graph](/training_results/best_fit/results.png)
- **Sample Training Batches:**
  - ![Train Batch 0](/training_results/best_fit/train_batch0.jpg)
  - ![Train Batch 1](/training_results/best_fit/train_batch1.jpg)
  - ![Train Batch 1890](/training_results/best_fit/train_batch1890.jpg)
  - ![Train Batch 1891](/training_results/best_fit/train_batch1891.jpg)
  - ![Train Batch 1892](/training_results/best_fit/train_batch1892.jpg)
  - These images show training samples with bounding boxes.
- **Validation Predictions:**
  - ![Val Batch 0 Labels](/training_results/best_fit/val_batch0_labels.jpg) ![Val Batch 0 Pred](/training_results/best_fit/val_batch0_pred.jpg)
  - ![Val Batch 1 Labels](/training_results/best_fit/val_batch1_labels.jpg) ![Val Batch 1 Pred](/training_results/best_fit/val_batch1_pred.jpg)
  - ![Val Batch 2 Labels](/training_results/best_fit/val_batch2_labels.jpg) ![Val Batch 2 Pred](/training_results/best_fit/val_batch2_pred.jpg)
  - These images compare ground truth labels with model predictions.

### `detect/`
This folder is used for detection outputs and inference results.

### `Result.ipynb`
A Jupyter Notebook summarizing the results and visualizations from training and tuning.

## Notes
- The `tune/` folder contains hyperparameter tuning results, while `best_fit/` holds the final trained model metrics.
- Images within these folders provide valuable insights into the training and validation processes.
- Further details and analysis are provided in `Result.ipynb`.


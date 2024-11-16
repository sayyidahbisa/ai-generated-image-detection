# AI-Generated-Detections
```
```
This repository contains a project focused on detecting and classifying AI-generated and human-created images using a Convolutional Neural Network (CNN). The project employs Stratified K-Fold Cross-Validation (SKFCV) to improve model evaluation and reduce overfitting.

## Overview
The project leverages CNNs to classify images into two categories:
1. AI-generated images
2. Human-made images

The dataset, sourced from Kaggle, contains 18,618 images (10,330 AI-generated and 8,288 human-made). The focus is to enhance model performance by addressing overfitting through SKFCV.

Key Objectives:
- Compare performance of models trained with and without SKFCV.
- Experiment with data augmentation techniques.
- Evaluate the model using metrics like Precision, Recall, F1-Score, and ROC AUC.

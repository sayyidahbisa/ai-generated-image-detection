# AI-Generated-Detections

This repository contains a project focused on detecting and classifying AI-generated and human-created images using a Convolutional Neural Network (CNN). The project employs Stratified K-Fold Cross-Validation (SKFCV) to improve model evaluation and reduce overfitting.

## Overview
The project leverages CNNs to classify images into two categories:
1. AI-generated images
2. Human-made images

The dataset, sourced from Kaggle, contains 18,618 images (10,330 AI-generated and 8,288 human-made). The focus is to enhance model performance by addressing overfitting through SKFCV.

Key Objectives:
- Compare the performance of models trained with and without SKFCV.
- Focus on reducing overfitting during model development.
- Hyperparameter Tuning improvement model architecture.
- Evaluate the model using metrics like Precision, Recall, F1-Score, and ROC AUC.

Features
- CNN-based binary image classification.
- Implementation of Stratified K-Fold Cross-Validation (SKFCV).
- Hyperparameter tuning to optimize the model.
- Streamlit-based deployment for user interaction.

## Results
CNN Only
<img width="901" alt="image" src="https://github.com/user-attachments/assets/79cc7ea1-94b2-4b0a-aa83-43c75f6cf6b5">

CNN + SKFCV
![image](https://github.com/user-attachments/assets/cb766c6a-08c2-495a-b5bd-2f5aeb3ec620)



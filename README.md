# Trichomonas Detection Research with DCNN-Xception, Encoder-Decoder, & Canny

## Description
This project was developed as part of our undergraduate thesis that focuses on developing deep learning models integrating DCNN-Xception and Encoder-Decoder architectures with Canny Edge Detection to identify **Trichomonas vaginalis** in microscopic images. The models achieved impressive accuracy rates of 91% and 93%, respectively. Key contributions include fine-tuning the architecture, experimenting with and training the models, evaluating performance metrics, optimizing classification through data augmentation, and constructing the research framework.

---

## Dataset
### Source
- **[TVMI3K](https://zenodo.org/records/6792861)** (Li et al., 2022)
- **[MVDI25K](https://zenodo.org/records/5523661)** (Li et al., 2021)
- **[Video-to-Image Dataset](https://github.com/wxz92/Trichomonas-Vaginalis-Detection)** (Wang et al., 2021)

### Description
Three datasets were used:
1. **TVMI3K**: Contains 2,524 positive images of Trichomonas vaginalis and 634 negative background images, enhancing the models' generalization ability.
2. **MVDI25K**: Comprises 25,708 images across ten object classes, with 912 specifically annotated as containing Trichomonas vaginalis (positive).
3. **Video-to-Image Dataset**: Features images generated from video sources to provide additional variety and complexity for training.

---

## License
The dataset used in this project is in the public domain and free to use without restrictions.

---

## Features
- **Data Preprocessing**: Includes cleaning, augmentation, and Canny edge detection.
- **Model Training**: Leveraged DCNN-Xception and Encoder-Decoder architectures with hyperparameter tuning.
- **Performance Evaluation**: Measured accuracy, precision, recall, and F1-score.
- **User Interface Testing**: Designed and tested a user-friendly interface for model integration.

---

## Repository Overview

This repository contains the following files:
- **Model Files**: These include pre-trained models in Keras format (e.g., `dcnn_base.keras`, `dcnn_canny.keras`, `encoder_base.keras`, `encoder_canny.keras`).
- **GUI Code Files**: The repository includes Python files (`.py`) and Jupyter Notebook files (`.ipynb`) to test the model.
- **Research Overview Presentation**: A presentation summarizing the research work is also included.

### How to Use the Model
In the provided Jupyter Notebook (`.ipynb`), users should change the path to their Google Drive folder where the model files are stored. Once the correct path is set, the models can be loaded and used for inference directly from the notebook.



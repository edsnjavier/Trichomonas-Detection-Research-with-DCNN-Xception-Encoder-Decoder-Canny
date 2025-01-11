# Trichomonas Detection Research with DCNN-Xception, Encoder-Decoder, & Canny

## Description
This project was developed as part of our undergraduate thesis that focuses on developing deep learning models integrating DCNN-Xception and Encoder-Decoder architectures with Canny Edge Detection to identify **Trichomonas vaginalis** in microscopic images. The models achieved impressive accuracy rates of 91% and 93%, respectively. Key contributions include fine-tuning the architecture, experimenting with and training the models, evaluating performance metrics, optimizing classification through data augmentation, and constructing the research framework.

---

## Dataset
### Source
- **TVMI3K** (Li et al., 2022)
- **MVDI25K** (Li et al., 2021)
- **Video-to-Image Dataset** (Wang et al., 2021)

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


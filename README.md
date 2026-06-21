# Brain Tumor Detection and Risk Prediction Using AI/ML

## Overview

Brain Tumor Detection and Risk Prediction is an Artificial Intelligence and Machine Learning project designed to assist in the early detection of brain tumors from MRI scans. The system uses a Convolutional Neural Network (CNN) to classify MRI images into different tumor categories and provides a graphical interface for easy interaction.

In addition to tumor classification, the project includes a basic future risk assessment module that evaluates potential tumor risk based on family history and medical questionnaire responses.

---

## Features

### MRI-Based Brain Tumor Classification

The model classifies MRI images into four categories:

* Glioma Tumor
* Meningioma Tumor
* Pituitary Tumor
* No Tumor

### Image Preprocessing

* Image resizing
* Normalization of pixel values
* Batch preparation for prediction

### Tumor Localization

* Displays a bounding box around the detected tumor region
* Provides approximate tumor location coordinates

### Future Risk Assessment

A questionnaire-based module evaluates:

* Family history of brain tumors
* Abnormal blood test results
* Neurological symptoms
* Headaches
* Dizziness and seizures

### Graphical User Interface

* Built using Tkinter
* Easy MRI image upload and analysis
* Displays prediction results visually

---

## System Workflow

1. MRI image is provided as input.
2. Image preprocessing is performed.
3. CNN model analyzes the MRI scan.
4. Tumor type is predicted.
5. If a tumor is detected:

   * Tumor location is highlighted.
   * Prediction results are displayed.
6. If no tumor is detected:

   * User completes a risk assessment questionnaire.
   * Future tumor risk is estimated.

---

## Technologies Used

| Technology       | Purpose               |
| ---------------- | --------------------- |
| Python           | Programming Language  |
| TensorFlow/Keras | Deep Learning Model   |
| OpenCV           | Image Processing      |
| NumPy            | Numerical Computation |
| Scikit-Learn     | Dataset Splitting     |
| Tkinter          | GUI Development       |
| PIL (Pillow)     | Image Display         |
| CNN              | Image Classification  |

---

## Dataset

The dataset consists of MRI brain scan images categorized into:

* Glioma
* Meningioma
* Pituitary
* No Tumor

The images are organized into separate folders corresponding to each class.

Dataset Structure:

data/
│
├── glioma/
├── meningioma/
├── no_tumor/
└── pituitary/

---

## Model Architecture

The project uses a Convolutional Neural Network (CNN) consisting of:

### Convolution Layer 1

* 32 Filters
* 3×3 Kernel
* ReLU Activation

### Max Pooling Layer

### Convolution Layer 2

* 64 Filters
* 3×3 Kernel
* ReLU Activation

### Max Pooling Layer

### Convolution Layer 3

* 128 Filters
* 3×3 Kernel
* ReLU Activation

### Max Pooling Layer

### Fully Connected Layer

* 128 Neurons
* ReLU Activation

### Output Layer

* Softmax Activation
* 4 Output Classes

---

## Project Structure

Brain-Tumor-Detection/

│

├── train_model.py

├── predict_tumor.py

├── gui_application.py

├── brain_tumor_model.keras

├── dataset/

│ ├── glioma/

│ ├── meningioma/

│ ├── no_tumor/

│ └── pituitary/

│

└── README.md

---

## Installation

### Clone Repository

```bash
git clone https://github.com/your-username/brain-tumor-detection.git

cd brain-tumor-detection
```

### Install Dependencies

```bash
pip install tensorflow
pip install numpy
pip install opencv-python
pip install pillow
pip install scikit-learn
```

---

## Training the Model

Run:

```bash
python train_model.py
```

This will:

* Load MRI images
* Train the CNN model
* Save the trained model as:

```bash
brain_tumor_model.keras
```

---

## Running Predictions

Run:

```bash
python predict_tumor.py
```

The model will:

* Load the MRI image
* Predict tumor type
* Display tumor location information

---

## Launching the GUI

Run:

```bash
python gui_application.py
```

Features available:

* Upload MRI image
* Predict tumor type
* Visualize tumor region
* Complete future risk assessment questionnaire

---

## Sample Output

```text
Predicted Tumor Type: Glioma

Tumor Location:
x1 = 50
y1 = 50
x2 = 150
y2 = 150
```

### Future Risk Assessment

```text
Future Tumor Risk:
Low Risk of Developing Brain Tumor
```

---

## Future Enhancements

* Real tumor segmentation using U-Net
* Improved localization accuracy
* Web-based deployment using Flask or Django
* Mobile application integration
* Medical report generation
* Risk prediction using clinical and genetic datasets
* Explainable AI (XAI) visualizations
* Integration with hospital management systems

---

## Applications

* Medical imaging assistance
* Preliminary brain tumor screening
* Clinical decision support systems
* Healthcare research
* Educational and academic projects

---

## Contributors

* Malishka Paradkar
* Team Members

(Add all contributor names here)

---

## Disclaimer

This project is intended for educational and research purposes only. It should not be used as a substitute for professional medical diagnosis or treatment.

---

## License

This project is licensed under the MIT License.

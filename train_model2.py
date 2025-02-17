import os
import numpy as np
import cv2
import tensorflow as tf
from sklearn.model_selection import train_test_split
from tensorflow.keras import layers, models
from tensorflow.keras.preprocessing.image import ImageDataGenerator

# Set up paths for the dataset
image_folder = "/Applications/Coding/MindScan/data2/test"
categories = ['glioma', 'meningioma', 'no_tumor', 'pituitary']

# Load and preprocess data
def load_data(image_folder):
    data = []
    labels = []
    for category in categories:
        category_path = os.path.join(image_folder, category)
        # Check if the folder exists
        if not os.path.exists(category_path):
            print(f"Category folder {category_path} does not exist.")
            continue
        
        for img_name in os.listdir(category_path):
            img_path = os.path.join(category_path, img_name)
            
            # Read the image
            img = cv2.imread(img_path)
            
            # Check if the image was loaded successfully
            if img is None:
                print(f"Warning: Failed to load image {img_path}. Skipping.")
                continue  # Skip the invalid image
            
            # Resize the image to a consistent size
            img_resized = cv2.resize(img, (128, 128))  # Resize to 128x128 pixels
            
            # Normalize the image
            img_normalized = img_resized / 255.0  # Scale pixel values between 0 and 1
            
            # Append the image and its corresponding label
            data.append(img_normalized)
            labels.append(categories.index(category))  # Map category to its index label
            
    return np.array(data), np.array(labels)

# Load data
X, y = load_data(image_folder)

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Build a CNN model for tumor detection and segmentation
model = models.Sequential([
    layers.Conv2D(32, (3, 3), activation='relu', input_shape=(128, 128, 3)),
    layers.MaxPooling2D((2, 2)),
    layers.Conv2D(64, (3, 3), activation='relu'),
    layers.MaxPooling2D((2, 2)),
    layers.Conv2D(128, (3, 3), activation='relu'),
    layers.MaxPooling2D((2, 2)),
    layers.Flatten(),
    layers.Dense(128, activation='relu'),
    layers.Dense(len(categories), activation='softmax')  # Output layer for category prediction
])

# Compile the model
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# Train the model
model.fit(X_train, y_train, epochs=10, batch_size=32, validation_data=(X_test, y_test))

# Save the model
model.save("brain_tumor_model.keras")




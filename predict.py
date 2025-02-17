import tensorflow as tf
import numpy as np
import cv2
from PIL import Image


model.save("brain_tumor_model.keras")

tumor_classes = ["Glioma", "Meningioma", "No Tumor", "Pituitary"]

def preprocess_image(image_path):
    img = Image.open(image_path).convert("RGB")
    img = img.resize((224, 224))
    img = np.array(img) / 255.0
    img = np.expand_dims(img, axis=0)  # Model expects batch input
    return img

def predict(image_path):
    image = preprocess_image(image_path)
    prediction = model.predict(image)
    
    predicted_class = tumor_classes[np.argmax(prediction)]
    confidence = round(np.max(prediction) * 100, 2)
    
    return f"Prediction: {predicted_class}, Confidence: {confidence}%"

# Test the model
image_path = "/Users/rudranisarkar/Documents/data2/test/glioma/Te-gl_0010.jpg"
print(predict(image_path))
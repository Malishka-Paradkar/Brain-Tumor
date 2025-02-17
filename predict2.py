import cv2
import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing import image

# Load the trained model (updated to .keras format)
model = tf.keras.models.load_model('brain_tumor_model.keras')

# Function for prediction from MRI image
def predict_tumor(image_path):
    img = cv2.imread(image_path)
    
    # Check if the image was loaded properly
    if img is None:
        raise ValueError(f"Image at {image_path} could not be loaded.")
    
    img_resized = cv2.resize(img, (224, 224))  # Resize the image to 224x224 (expected size by model)
    img_normalized = img_resized / 255.0  # Normalize the image (scaling pixel values between 0 and 1)
    img_reshaped = np.expand_dims(img_normalized, axis=0)  # Add batch dimension (shape becomes (1, 224, 224, 3))

    # Predict the class
    prediction = model.predict(img_reshaped)
    class_index = np.argmax(prediction)
    class_name = ['glioma', 'meningioma', 'no_tumor', 'pituitary'][class_index]
    
    # Tumor detection and segmentation if class is not 'no_tumor'
    if class_name != 'no_tumor':
        tumor_location = detect_tumor(img)  # Call your segmentation model here for tumor detection
        return class_name, tumor_location
    else:
        return class_name, None

# Dummy tumor location detection function (bounding box for now)
def detect_tumor(image):
    # For simplicity, returning a dummy bounding box (just for illustration)
    return {"x1": 50, "y1": 50, "x2": 150, "y2": 150}  # Coordinates of the bounding box

# Blood test and family genetics quiz for future predictions
def future_tumor_risk(answers):
    risk_score = 0
    for answer in answers:
        risk_score += answer  # Just a simple sum of responses, improve this logic
    if risk_score > 5:
        return "High risk of developing brain tumor in the future."
    else:
        return "Low risk of developing brain tumor in the future."

# Sample input: MRI Image and Patient quiz data
image_path = '/Applications/Coding/MindScan/data2/test/notumor/Te-no_0010.jpg'
try:
    predicted_class, tumor_location = predict_tumor(image_path)
    print(f"Predicted tumor type: {predicted_class}")
    if tumor_location:
        print(f"Tumor detected at location: {tumor_location}")
except ValueError as e:
    print(e)

# Sample family history and blood test quiz (for prediction of future risk)
patient_answers = [1, 0, 1, 0, 1]  # Example answers from the patient
future_risk = future_tumor_risk(patient_answers)
print(f"Future tumor risk: {future_risk}")

# Simple quiz questions for the patient
def family_genetics_and_blood_test_quiz():
    questions = [
        "Do you have a family history of brain tumors? (1 for Yes, 0 for No): ",
        "Have you had abnormal blood test results? (1 for Yes, 0 for No): ",
        "Have you had unexplained headaches? (1 for Yes, 0 for No): ",
        "Do you experience dizziness or seizures? (1 for Yes, 0 for No): ",
        "Have you ever had any neurological conditions? (1 for Yes, 0 for No): ",
    ]
    
    answers = []
    for question in questions:
        answer = int(input(question))
        answers.append(answer)
    
    return answers

# Example usage:
answers = family_genetics_and_blood_test_quiz()
future_risk = future_tumor_risk(answers)
print(f"Future risk of brain tumor: {future_risk}")





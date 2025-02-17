import numpy as np
import tensorflow as tf
import tkinter as tk
from tkinter import messagebox
from tensorflow.keras.preprocessing import image
from PIL import Image, ImageTk

# Load the trained model (updated to .keras format)
model = tf.keras.models.load_model('brain_tumor_model.keras')

# Function for prediction from MRI image
def predict_tumor(image_path):
    img = Image.open(image_path)
    
    # Check if the image was loaded properly
    if img is None:
        raise ValueError(f"Image at {image_path} could not be loaded.")
    
    img_resized = img.resize((224, 224))  # Resize the image to 224x224 (expected size by model)
    img_normalized = np.array(img_resized) / 255.0  # Normalize the image (scaling pixel values between 0 and 1)
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

# GUI Logic to directly load an image without a dialog
def open_image():
    # Specify the path to the image you want to use directly
    file_path = "/path/to/your/image.jpg"  # <-- Replace with your image path
    
    if file_path:
        try:
            predicted_class, tumor_location = predict_tumor(file_path)
            display_results(predicted_class, tumor_location, file_path)
        except ValueError as e:
            messagebox.showerror("Error", f"Error: {e}")

def display_results(predicted_class, tumor_location, image_path):
    result_window = tk.Toplevel(root)
    result_window.title("Prediction Results")

    label_class = tk.Label(result_window, text=f"Predicted Tumor Type: {predicted_class}")
    label_class.pack()

    if tumor_location:
        label_location = tk.Label(result_window, text=f"Tumor Location: x1={tumor_location['x1']}, y1={tumor_location['y1']}, x2={tumor_location['x2']}, y2={tumor_location['y2']}")
        label_location.pack()

        # Display the image with a bounding box
        img = Image.open(image_path)
        img_resized = img.resize((224, 224))  # Resize image to fit in display window
        img_pil = np.array(img_resized)
        
        # Draw bounding box
        img_pil[tumor_location['y1']:tumor_location['y2'], tumor_location['x1']:tumor_location['x2']] = [0, 255, 0]  # Mark bounding box area in green
        
        img_tk = ImageTk.PhotoImage(image=Image.fromarray(img_pil))

        panel = tk.Label(result_window, image=img_tk)
        panel.image = img_tk  # keep a reference
        panel.pack()
    else:
        label_location = tk.Label(result_window, text="No tumor detected.")
        label_location.pack()

        # Family history and blood test quiz
        family_genetics_risk(result_window)

def family_genetics_risk(result_window):
    def submit_answers():
        answers = [var.get() for var in answer_vars]
        future_risk_message = future_tumor_risk(answers)
        label_risk.config(text=f"Future tumor risk: {future_risk_message}")
    
    label = tk.Label(result_window, text="Please answer the following questions:")
    label.pack()

    questions = [
        "Do you have a family history of brain tumors? (1 for Yes, 0 for No)",
        "Have you had abnormal blood test results? (1 for Yes, 0 for No)",
        "Have you had unexplained headaches? (1 for Yes, 0 for No)",
        "Do you experience dizziness or seizures? (1 for Yes, 0 for No)",
        "Have you ever had any neurological conditions? (1 for Yes, 0 for No)"
    ]

    answer_vars = []
    for question in questions:
        var = tk.IntVar()
        answer_vars.append(var)
        checkbox = tk.Checkbutton(result_window, text=question, variable=var)
        checkbox.pack()

    submit_button = tk.Button(result_window, text="Submit Answers", command=submit_answers)
    submit_button.pack()

    label_risk = tk.Label(result_window, text="Future tumor risk: ")
    label_risk.pack()

# Setup GUI
root = tk.Tk()
root.title("Brain Tumor Detection and Risk Prediction")
root.geometry("600x400")

open_button = tk.Button(root, text="Open MRI Image", command=open_image)
open_button.pack(pady=20)

root.mainloop()



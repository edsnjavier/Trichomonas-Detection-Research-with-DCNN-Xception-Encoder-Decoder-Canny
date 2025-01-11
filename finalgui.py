import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from tkinter.ttk import Style
from ttkbootstrap import Style
from PIL import Image, ImageTk
import os
import sys
import cv2
import tensorflow as tf
from tensorflow.keras.models import load_model

# Get the correct path for model files based on whether the app is bundled or in development
def get_model_path(model_name):
    if getattr(sys, 'frozen', False):  # Check if the app is frozen (i.e., running as an executable)
        return os.path.join(sys._MEIPASS, 'models', model_name)
    else:  # For development, use the local paths
        return os.path.join('C:/Users/reiva/Downloads/models', model_name)

# Define model paths
dcnn = get_model_path('dcnn_base.keras')
encoder = get_model_path('encoder_base.keras')
dcnn_canny = get_model_path('dcnn_canny.keras')
encoder_canny = get_model_path('encoder_canny.keras')

# Load models
dcnn_xception_model = load_model(dcnn, compile=False)
encoder_decoder_model = load_model(encoder, compile=False)
dcnn_xception_canny_model = load_model(dcnn_canny, compile=False)
encoder_decoder_canny_model = load_model(encoder_canny, compile=False)

# Validate image extensions
def validate_image(file_path):
    allowed_extensions = ['.png', '.jpg', '.jpeg']
    _, ext = os.path.splitext(file_path)
    return ext.lower() in allowed_extensions

# Apply Canny edge detection
def apply_canny_and_blend(image_path, alpha=0.25):
    image = cv2.imread(image_path)
    if image is None:
        raise ValueError("Invalid image. Ensure the file path is correct and the file is an image.")
    
    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 65, 100)

    # Convert to 3-channel image
    edges_3_channel = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)

    # Resize edges to match the original image (if necessary)
    if image.shape != edges_3_channel.shape:
        edges_3_channel = cv2.resize(edges_3_channel, (image.shape[1], image.shape[0]))

    # Perform alpha blending
    blended_image = cv2.addWeighted(image, 1 - alpha, edges_3_channel, alpha, 0)
    return blended_image

# Predict images
def predict():
    image_path = file_path_var.get()
    model_choice = model_var.get()
    canny_choice = canny_var.get()

    if not image_path:
        messagebox.showerror("Error", "Please upload an image.")
        return

    # Validate image extension
    if not validate_image(image_path):
        messagebox.showerror("Error", "Invalid file type. Allowed file types: PNG, JPG, JPEG.")
        return

    try:
        # Apply Canny edge detection and blending if selected
        if canny_choice == "With Canny":
            blended_image = apply_canny_and_blend(image_path)
            img = Image.fromarray(cv2.cvtColor(blended_image, cv2.COLOR_BGR2RGB))
        else:
            img = Image.open(image_path).convert("RGB")

        # Resize image based on selected model
        if model_choice == "DCNN-Xception":
            img = img.resize((299, 299))
            model = dcnn_xception_canny_model if canny_choice == "With Canny" else dcnn_xception_model
        elif model_choice == "Encoder-Decoder":
            img = img.resize((224, 224))
            model = encoder_decoder_canny_model if canny_choice == "With Canny" else encoder_decoder_model
        else:
            messagebox.showerror("Error", "Invalid model choice.")
            return

        # Convert image to array
        img_array = tf.keras.preprocessing.image.img_to_array(img)
        img_array = tf.expand_dims(img_array, 0)

        # Make predictions using the selected model
        predictions = model.predict(img_array)

        # Decode predictions into percentages
        negative, positive = tuple(predictions[0])

        # Determine the class with the highest value and show output
        if positive > negative:
            result = f"This image is positive ({positive * 100:.2f}% confidence). Suggestion: Parasite found. Consider further investigation."
        else:
            result = f"This image is negative ({negative * 100:.2f}% confidence). No parasite detected."
        
        result_label.config(text=result)

    except Exception as e:
        messagebox.showerror("Error", f"Error processing image: {e}")

# For uploading images
def upload_image():
    file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
    if file_path: 
        file_path_var.set(file_path)
        try:
            image = Image.open(file_path)  # Open the image
            img_width = 100
            img_height = 100
            img_tk = ImageTk.PhotoImage(image)  # Convert the image to a Tkinter-compatible format
            image_label.config(width=img_width, height=img_height) # Update image label size dynamically
            image_label.config(image=img_tk)  # Set the image in the label
            image_label.image = img_tk  # Keep a reference to the image
        except Exception as e:
            messagebox.showerror("Error", f"Error loading image: {e}")

# Resets the interface
def reset():
    file_path_var.set("")
    model_var.set("---")
    canny_var.set("Without Canny")
    image_label.config(image="", text="Image Preview", width=20, height=5)
    result_label.config(text="Prediction result is shown here.")

# Tkinter GUI
root = tk.Tk()
root.title("DATASCI10 - Trichomonas Vaginalis Detection")
root.geometry("800x600")
root.resizable(True, True)

# Apply a theme
style = Style()
style.theme_use('darkly')

# Main Frame
main_frame = tk.Frame(root)
main_frame.pack(expand=True, fill="both", padx=20, pady=20)

# Title and subtitle of app
title = tk.Label(
    main_frame,
    text="Detection of Trichomonas vaginalis in Microscopic Images Using DCNN-Xception with Canny Edge Detection",
    font=("Helvetica", 18, "bold"),
    wraplength=500,
    justify="center",
)
title.pack(pady=10)

subtitle = tk.Label(
    main_frame,
    text="University of Santo Tomas College of Information and Computing Sciences\nGuevarra, Javier, Tapao (2024)",
    font=("Helvetica", 12),
    justify="center",
)
subtitle.pack(pady=10)

# Initial variables
file_path_var = tk.StringVar()
model_var = tk.StringVar(value="---")
canny_var = tk.StringVar(value="Without Canny")

# Frames inside the main frame
form_frame = tk.Frame(main_frame)
form_frame.pack(pady=20)

# Image upload button
upload_button = tk.Button(form_frame, text="Upload Image", command=upload_image, width=20)
upload_button.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

# Image preview label
image_label = tk.Label(form_frame, text="Image Preview", font=("Helvetica", 10), width=20, height=5, relief="solid")
image_label.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

# Frame for the left side (Model select and Canny select)
left_frame = tk.Frame(form_frame)
left_frame.grid(row=2, column=0, padx=10, pady=10, sticky="w")

# Frame for the right side (Predict and Reset buttons)
right_frame = tk.Frame(form_frame)
right_frame.grid(row=2, column=1, padx=10, pady=10, sticky="e")

# Model selection dropdown
model_label = tk.Label(left_frame, text="Select Model:")
model_label.grid(row=0, column=0, padx=10, pady=10, sticky="e")
model_choices = ["---", "DCNN-Xception", "Encoder-Decoder"]
model_menu = ttk.Combobox(left_frame, textvariable=model_var, values=model_choices, width=20)
model_menu.grid(row=0, column=1, padx=10, pady=10)

# Canny edge detection dropdown
canny_label = tk.Label(left_frame, text="Canny Edge Detection:")
canny_label.grid(row=1, column=0, padx=10, pady=10, sticky="e")
canny_choices = ["Without Canny", "With Canny"]
canny_menu = ttk.Combobox(left_frame, textvariable=canny_var, values=canny_choices, width=20)
canny_menu.grid(row=1, column=1, padx=10, pady=10)

# Predict button 
predict_button = tk.Button(right_frame, text="Predict", command=predict, width=20)
predict_button.grid(row=0, column=0, padx=10, pady=10)

# Reset button
reset_button = tk.Button(right_frame, text="Reset", command=reset, width=20)
reset_button.grid(row=1, column=0, padx=10, pady=10)

# Result label
result_label = tk.Label(
    form_frame,
    text="Prediction result is shown here.",
    font=("Helvetica", 10),
    justify="center",
    relief="solid",
    padx=20, 
    pady=10,   
    width=80
)
result_label.grid(row=3, column=0, columnspan=2, pady=10)

# Run the app
root.mainloop()
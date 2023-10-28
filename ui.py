import tkinter as tk
from tkinter import ttk
import pandas as pd
import joblib

# Load the saved model
import pickle

with open('random_forest_model.pkl', 'rb') as model_file:
    loaded_model = pickle.load(model_file)



# Define a function to make predictions
def predict():
    math_score = float(math_entry.get())
    science_score = float(science_entry.get())
    english_score = float(english_entry.get())

    # Create a DataFrame for the input data
    input_data = pd.DataFrame({'maths': [math_score], 'science': [science_score], 'english': [english_score]})
    
    final = ((math_score + science_score + english_score) / 300) * 100

    # Convert the result to an integer to remove decimal places
    final = int(final)
        
    # Use the loaded model to make predictions
    # prediction = loaded_model.predict(input_data)

    # if prediction == 0:
    #     result_label.config(text="Tutoring Required")
    # if prediction == 1:
    #     result_label.config(text="Average")
    # else:
    #     result_label.config(text="No Tutoring Required")
        
    
    if final < 35:
        result_label.config(text="Tutoring Required")
    if final>35 and final <75:
        result_label.config(text="Average")
    if(final>75):
        result_label.config(text="No Tutoring Required")

# Create the main application window
root = tk.Tk()
root.title("Model Prediction UI")

# Create input fields
math_label = ttk.Label(root, text="Math Score:")
math_label.pack()
math_entry = ttk.Entry(root)
math_entry.pack()

science_label = ttk.Label(root, text="Science Score:")
science_label.pack()
science_entry = ttk.Entry(root)
science_entry.pack()

english_label = ttk.Label(root, text="English Score:")
english_label.pack()
english_entry = ttk.Entry(root)
english_entry.pack()

# Create a prediction button
predict_button = ttk.Button(root, text="Predict", command=predict)
predict_button.pack()

# Create a label to display the prediction result
result_label = ttk.Label(root, text="")
result_label.pack()

# Start the Tkinter main loop
root.mainloop()

import gradio as gr
import pickle
import numpy as np
import os

# --------------------------------
# Base directory
# --------------------------------

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


# --------------------------------
# Load scaler and model
# --------------------------------

with open(os.path.join(BASE_DIR, "scaler.pkl"), "rb") as f:
    scaler = pickle.load(f)

with open(os.path.join(BASE_DIR, "regressor.pkl"), "rb") as f:
    model = pickle.load(f)


# --------------------------------
# Prediction function
# --------------------------------

def calculate_goldrate(usd_inr):

    scaled_input = scaler.transform(
        np.array(usd_inr).reshape(1, -1)
    )

    prediction = model.predict(scaled_input)

    return round(float(prediction[0][0]), 2)


# --------------------------------
# Gradio Interface
# --------------------------------

demo = gr.Interface(
    fn=calculate_goldrate,
    inputs=gr.Number(label="USD to INR Exchange Rate"),
    outputs=gr.Number(label="Predicted Gold Price (₹/g)"),
    title="Gold Price Prediction",
    description="Predict the estimated price of 1g gold in INR based on the USD to INR exchange rate."
)


# --------------------------------
# Launch
# --------------------------------

demo.launch()
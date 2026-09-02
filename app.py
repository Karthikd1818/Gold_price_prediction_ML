import gradio as gr
import pickle
import numpy as np
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

scaler = pickle.load(open('scaler.pkl','rb'))
model = pickle.load(open('regressor.pkl','rb'))

def calculate_goldrate(usd_inr):
    scaled_input = scaler.transform(np.array(usd_inr).reshape(1,-1))
    return round(model.predict(scaled_input)[0][0],2)

demo = gr.Interface(
    fn=calculate_goldrate,
    inputs=["number"],
    outputs=["number"],
    title="How much is 1g gold now in INR based on USD to INR exchange rate?"
)

demo.launch(share=True)
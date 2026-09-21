# 🪙 22K Gold Price Prediction using Simple Linear Regression

## 📌 Project Overview

This project uses **Simple Linear Regression** to predict the **22K gold price per gram in India** based on the **USD to INR exchange rate**.

The project demonstrates a complete basic machine learning workflow, including data preprocessing, exploratory analysis, model training, evaluation, and prediction.

## 🎯 Objective

The main objective is to build a simple regression model that can estimate the price of **22K gold per gram in INR** using the USD-INR exchange rate as the input feature.

## 🛠️ Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Scikit-learn
* Jupyter Notebook
* Gradio

## 🤖 Machine Learning Algorithm

### Simple Linear Regression

Simple Linear Regression is used to model the relationship between:

**Input Feature:**

* USD to INR Exchange Rate

**Target Variable:**

* 22K Gold Price per Gram in INR

The model learns the relationship between the exchange rate and gold price and uses it to generate predictions.

## 🔄 Machine Learning Workflow

```text
Raw Data
   ↓
Data Loading
   ↓
Data Cleaning & Preprocessing
   ↓
Exploratory Data Analysis
   ↓
Feature Selection
   ↓
Train-Test Split
   ↓
Simple Linear Regression
   ↓
Model Evaluation
   ↓
Gold Price Prediction
   ↓
Gradio Application
```

## 📊 Project Steps

### 1. Data Loading

Loaded the dataset using Pandas and inspected its structure, data types, and statistical properties.

### 2. Data Preprocessing

* Checked for missing values
* Checked for duplicate records
* Verified data types
* Prepared the required input and target variables

### 3. Exploratory Data Analysis

Analyzed the relationship between the USD-INR exchange rate and the 22K gold price using data visualization and correlation analysis.

### 4. Model Training

The dataset was divided into training and testing sets, followed by training a Simple Linear Regression model using Scikit-learn.

### 5. Model Evaluation

The model was evaluated using regression metrics such as:

* **R² Score**
* **Mean Absolute Error (MAE)**
* **Mean Squared Error (MSE)**
* **Root Mean Squared Error (RMSE)**

> Add your actual metric values here after confirming the final model results.

## 📈 Prediction

The trained model takes a **USD-INR exchange rate** as input and predicts the estimated **22K gold price per gram in Indian Rupees**.

Example:

```text
Input:
USD-INR Exchange Rate

Output:
Predicted 22K Gold Price per Gram (INR)
```

## 🌐 Gradio Application

A simple **Gradio interface** was created to allow users to enter the USD-INR exchange rate and receive the predicted 22K gold price per gram.

### Application Flow

```text
User enters USD-INR rate
          ↓
      ML Model
          ↓
Predicted 22K Gold Price
```

## 📂 Project Structure

```text
Simple-Linear-Regression-Gold-Price-Prediction/
│
├── data/
│   └── dataset.csv
│
├── notebook/
│   └── gold_price_prediction.ipynb
│
├── app.py
├── requirements.txt
└── README.md
```

> Update the file and folder names above to exactly match your actual repository structure.

## 🚀 How to Run the Project

### 1. Clone the repository

```bash
git clone https://github.com/Karthikd1818/Simple-Linear-Regression-Gold-Price-Prediction.git
```

### 2. Navigate to the project folder

```bash
cd Simple-Linear-Regression-Gold-Price-Prediction
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the application

```bash
python app.py
```

## ⚠️ Disclaimer

This project is developed for **educational and machine learning practice purposes**.

The predicted gold price is an **estimated model output** and should not be considered a real-time market price or financial advice.

## 👨‍💻 Author

**Karthik D**

Aspiring Data Scientist | Python | SQL | Machine Learning

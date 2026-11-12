# Gold Price Prediction in INR using the USD/INR Exchange Rate

A small machine learning project that predicts the gold rate (in INR) from the weekly USD/INR exchange rate, using simple linear regression. The model is also available as a small Gradio web app.

> **Project type:** Learning project. It uses only one input feature, so it shows the full regression workflow but is **not** a reliable tool for real gold price forecasting. See [Limitations](#limitations).

---

## Problem

Gold prices in India move with the international gold price and the rupee exchange rate. This project checks how much of the weekly gold rate in INR can be explained by the USD/INR rate alone.

## Dataset

| Item | Details |
|---|---|
| Period | Weekly data, 1 Jan 2024 to 30 Dec 2024 |
| Rows | 53 weekly records |
| USD/INR | Weekly closing rate downloaded from Yahoo Finance using `yfinance` (`USDINR=X`) |
| Gold rate | Gold rate in INR per gram, from `Gold vs USDINR.csv`. Source: **[ADD THE SOURCE OF THE GOLD RATE DATA]** |
| USD/INR range | 82.75 to 85.79 |

Data preparation:
- The gold rate was stored as text with the rupee sign and commas (for example `₹5,066.31`). I removed these symbols and converted the column to numbers.
- No missing values were found. No categorical columns needed encoding.
- Boxplots were used to check outliers.

## Method

1. Loaded the data and cleaned the gold rate column.
2. Explored the relationship with boxplots and a regression plot.
3. Split the data into 90% train (47 rows) and 10% test (6 rows), `random_state=42`.
4. Scaled the input with `StandardScaler`, fitted on the training data only.
5. Trained a `LinearRegression` model.
6. Evaluated on the test set with MSE, RMSE, MAE and R².
7. Tried `RandomizedSearchCV` on the model settings.
8. Saved the model and scaler with `pickle` and built a Gradio app.

## Results

Evaluated on the 6 test rows:

| Metric | Value |
|---|---|
| R² | 0.70 |
| MAE (average error) | about ₹309 per gram |
| MSE | 141,948 |
| RMSE | about ₹377 per gram |

In simple words: the USD/INR rate explains about 70% of the variation in the gold rate on this small test sample, and a typical prediction is off by roughly ₹309 per gram.

**Hyperparameter search:** `RandomizedSearchCV` selected `positive=True`. The resulting coefficient and intercept were the same as the original model (coefficient 469.21, intercept 5878.57 on the scaled input), so tuning did **not** improve this model. Linear regression has almost no settings that change the result.

## Web app (Gradio)

The last cell of the notebook launches a Gradio app. You enter a USD/INR value and it returns the predicted gold rate for 1 gram in INR.

```python
import gradio as gr
demo = gr.Interface(fn=calculate_gold_price, inputs=["number"], outputs=["number"])
demo.launch()
```

The app runs locally at `http://127.0.0.1:7860`. It is not deployed online.

## How to run

```bash
pip install yfinance pandas seaborn matplotlib scikit-learn gradio
jupyter notebook gold_price.ipynb
```

Files:
- `gold_price.ipynb` : full workflow
- `Gold vs USDINR.csv` : dataset
- `regressor.pkl`, `scaler.pkl` : created when you run the notebook

## Limitations

- **Only one feature.** Gold prices depend mainly on the international gold price, not just the exchange rate. This model ignores that, so it is a simple demonstration.
- **Very small data.** There are 53 rows and only 6 test rows, so the R² and error values can change a lot with a different split.
- **Random split on time data.** The rows are ordered by week, but the split was random, not by time. A real forecast should train on earlier weeks and test on later weeks.
- **Predictions outside the training range are unreliable.** The model was trained on USD/INR values between 82.75 and 85.79. For example, an input of 80 returns about ₹3,172, which is not a realistic gold rate.
- **One year only (2024).**

## Possible improvements

- Add the international gold price (USD per ounce) as a second feature.
- Use more years of data and a time-based train/test split.
- Compare with other models and report results with cross-validation.
- Deploy the Gradio app online (for example on Hugging Face Spaces).

## Author

Karthik D

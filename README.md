# ⚡ Electricity Fraud Prediction

This project uses machine learning techniques to detect potential cases of fraud in electricity consumption using meter data.

## 📂 Project content

- `notebooks/` : Jupyter notebooks for EDA, feature engineering and model design.
- `data/` : contains raw and processed data.
- `models/` : Saved trained models.
- `src/` : Python scripts for EDA, feature engineering and model prediction.
- `tests/` : Python scripts for testing the different steps of this ml project.
- `requirements.txt` : Python dependencies.

## 🧪 Algorithms used

- **Random Forest**
- **XGBoost**
- **LightGBM**
- **Logistic Regression**

## 📊 Important variables

The data contains variables such as :

- `customer_id`
- `meter_reading`
- `timestamp`
- `location`
- `fraud_flag`
- etc.


## 🎯 Goal

> Predict if a customer is a fraudster using historical cunsumption data.

## 🚀 Application

### Installation

```bash
git clone https://github.com/FranckKD/electricity-fraud-prediction.git
cd electricity-fraud-prediction
pip install -r requirements.txt
```
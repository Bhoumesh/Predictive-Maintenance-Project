# 🔧 Predictive Maintenance Using Machine Learning

## 📌 Overview

Predictive maintenance aims to predict equipment failures before they occur by analyzing sensor data.
This project uses Machine Learning to classify whether an industrial machine is likely to **fail** or operate **normally**, helping reduce downtime and maintenance costs.

The model is deployed using **Streamlit** as an interactive web application.

---

## 🎯 Problem Statement

Unexpected machine failures can cause:

* Production delays
* High maintenance costs
* Safety risks

This project predicts machine failure in advance using sensor parameters such as temperature, torque, rotational speed, and tool wear.

---

## 🧠 Machine Learning Approach

* **Type:** Binary Classification
* **Target Variable:** Machine Failure (0 = No Failure, 1 = Failure)
* **Algorithm Used:** Random Forest Classifier
* **Why Random Forest?**

  * Handles non-linear data well
  * Robust to noise
  * Provides high accuracy for tabular datasets

---

## 📊 Features Used

* Air temperature (K)
* Process temperature (K)
* Rotational speed (rpm)
* Torque (Nm)
* Tool wear (minutes)
* Temperature difference (engineered feature)
* Machine type (L, M)

---

## 🖥️ Web Application (Streamlit)

The Streamlit app allows users to:

* Enter machine sensor values
* Select machine type
* Instantly predict whether the machine is likely to fail

### Prediction Output:

* ✅ Machine is operating normally
* ⚠️ Machine is likely to fail soon

---

## 🛠️ Technologies & Tools

* Python
* Pandas, NumPy
* Scikit-learn
* Joblib
* Streamlit
* Git & GitHub

---

## 📂 Project Structure

```
Predictive-Maintenance-Project/
│
├── app.py                     # Streamlit application
├── notebook.ipynb             # Data analysis & model training
├── requirements.txt           # Dependencies
├── README.md                  # Project documentation
│
├── Data/
│   └── predictive_maintenance.csv
│
└── model/
    └── predictive_model.pkl   # Trained ML model
```

---

## 🚀 How to Run the Project Locally

### 1️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 2️⃣ Run Streamlit app

```bash
streamlit run app.py
```

---

## 📈 Results

* The model successfully predicts machine failure based on real-time inputs
* Helps demonstrate practical application of ML in industrial maintenance

---

## 🔮 Future Improvements

* Add failure probability percentage
* Add data visualization in Streamlit
* Deploy app on Streamlit Cloud
* Use advanced models like XGBoost

---

## 👤 Author

**Bhomesh Kr Dutta**
BSc Data Science Student

🔗 GitHub: [https://github.com/Bhoumesh](https://github.com/Bhoumesh)

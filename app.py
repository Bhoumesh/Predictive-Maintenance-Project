import streamlit as st
import pandas as pd
import joblib

# Load model
model = joblib.load("model/predictive_model.pkl")

# Page settings
st.set_page_config(page_title="Predictive Maintenance", layout="centered")

st.title("🔧 Predictive Maintenance System")
st.write("Predict machine failure using sensor data")

st.divider()

# Inputs
air_temp = st.number_input("Air Temperature (K)", 290.0, 310.0, 300.0)
process_temp = st.number_input("Process Temperature (K)", 300.0, 320.0, 310.0)
rot_speed = st.number_input("Rotational Speed (rpm)", 1000, 3000, 1500)
torque = st.number_input("Torque (Nm)", 0.0, 100.0, 40.0)
tool_wear = st.number_input("Tool Wear (min)", 0, 300, 100)

machine_type = st.selectbox("Machine Type", ["L", "M", "H"])

# Feature engineering
temp_diff = process_temp - air_temp

# Encoding (drop_first=True logic)
type_L = 1 if machine_type == "L" else 0
type_M = 1 if machine_type == "M" else 0

# Predict
if st.button("Predict Failure"):
    input_data = pd.DataFrame([{
        "Air temperature [K]": air_temp,
        "Process temperature [K]": process_temp,
        "Rotational speed [rpm]": rot_speed,
        "Torque [Nm]": torque,
        "Tool wear [min]": tool_wear,
        "Temp_diff": temp_diff,
        "Type_L": type_L,
        "Type_M": type_M
    }])

    prediction = model.predict(input_data)[0]

    if prediction == 1:
        st.error("⚠️ Machine is likely to FAIL soon!")
    else:
        st.success("✅ Machine is operating normally")

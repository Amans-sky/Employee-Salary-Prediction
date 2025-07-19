import streamlit as st
import joblib
import pandas as pd

# Load model
model = joblib.load("salary_predictor.pkl")

# Page Configuration
st.set_page_config(page_title="💼 Salary Predictor", layout="centered", page_icon="💰")

# Custom CSS with new background
st.markdown("""
    <style>
        body {
            background: linear-gradient(135deg, #e0f7fa, #e1f5fe);
            font-family: 'Segoe UI', sans-serif;
        }

        .main-container {
            background-color: white;
            padding: 3rem;
            border-radius: 15px;
            box-shadow: 0 8px 24px rgba(0, 0, 0, 0.1);
            margin-top: 30px;
        }

        h1 {
            color: #0d47a1;
            font-size: 2.5rem;
            text-align: center;
            margin-bottom: 0.5rem;
        }

        .subhead {
            text-align: center;
            font-size: 1.1rem;
            color: #555;
            margin-bottom: 2rem;
        }

        .stButton > button {
            background: linear-gradient(to right, #2196f3, #21cbf3);
            color: white;
            font-weight: bold;
            border-radius: 8px;
            padding: 0.6rem 1.2rem;
            transition: 0.3s;
            font-size: 1rem;
        }

        .stButton > button:hover {
            background: linear-gradient(to right, #1976d2, #26c6da);
            transform: scale(1.05);
        }

        .stSuccess {
            background-color: #d4edda;
            padding: 1rem;
            border-radius: 10px;
            color: #155724;
            font-weight: bold;
            font-size: 1.3rem;
            margin-top: 2rem;
            text-align: center;
        }

        label {
            font-weight: 500 !important;
            color: #0d47a1;
        }
    </style>
""", unsafe_allow_html=True)

# Main App UI
st.markdown("<div class='main-container'>", unsafe_allow_html=True)

st.title("💼 Salary Predictor")
st.markdown("<div class='subhead'>Predict an employee's estimated salary based on demographic and job-related inputs.</div>", unsafe_allow_html=True)

# Input form
def user_input():
    age = st.number_input("Age", 18, 70, 30)
    workclass = st.selectbox("Workclass", ["Private", "Self-emp-not-inc", "Local-gov", "State-gov", "Federal-gov"])
    education = st.selectbox("Education", ["Bachelors", "HS-grad", "11th", "Masters", "Some-college", "Assoc-acdm"])
    marital_status = st.selectbox("Marital Status", ["Never-married", "Married-civ-spouse", "Divorced"])
    occupation = st.selectbox("Occupation", ["Tech-support", "Craft-repair", "Other-service", "Sales", "Exec-managerial"])
    relationship = st.selectbox("Relationship", ["Husband", "Not-in-family", "Own-child", "Unmarried"])
    race = st.selectbox("Race", ["White", "Black", "Asian-Pac-Islander", "Amer-Indian-Eskimo"])
    gender = st.selectbox("Gender", ["Male", "Female"])
    hours_per_week = st.slider("Hours per Week", 1, 100, 40)

    data = {
        'age': [age],
        'workclass': [workclass],
        'fnlwgt': [200000],
        'education': [education],
        'educational-num': [10],
        'marital-status': [marital_status],
        'occupation': [occupation],
        'relationship': [relationship],
        'race': [race],
        'gender': [gender],
        'capital-gain': [0],
        'capital-loss': [0],
        'hours-per-week': [hours_per_week],
        'native-country': ['United-States']
    }

    return pd.DataFrame(data)

input_df = user_input()

# Predict Button
if st.button("🎯 Predict Salary"):
    prediction = model.predict(input_df)[0]
    st.success(f"💰 Estimated Salary: ₹{int(prediction):,}")

st.markdown("</div>", unsafe_allow_html=True)

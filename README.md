# Employee Salary Prediction

This project aims to predict an individual's salary based on demographic and work-related attributes using machine learning techniques. A Streamlit web application is also developed to make the model accessible for real-time predictions.

## 📌 Project Objectives

- Predict employee salaries using regression models.
- Preprocess and analyze the "Adult Census Income" dataset.
- Build and compare multiple regression models.
- Develop a user-friendly interface using Streamlit.

---

## 📂 Dataset

**Features include:**

- Age  
- Workclass  
- Education  
- Marital Status  
- Occupation  
- Relationship  
- Race  
- Gender  
- Hours per Week  
- Capital Gain / Loss  
- Native Country  

**Target:**  
- Salary (converted to numerical for regression)

---

## 🧪 Technologies & Libraries Used

- Python 3.x
- Pandas
- NumPy
- Scikit-learn
- Matplotlib / Seaborn (for visualization)
- Streamlit (for web deployment)
- Joblib (for model serialization)

---

## ⚙️ Project Workflow

1. **Data Collection**
   - Imported the Adult Census dataset.
2. **Exploratory Data Analysis (EDA)**
   - Summary statistics, missing values, visualizations.
3. **Data Preprocessing**
   - Imputation, one-hot encoding, feature scaling.
4. **Model Building**
   - Trained Linear Regression and Random Forest Regressor.
5. **Model Evaluation**
   - Metrics: RMSE, R² score.
6. **Streamlit Deployment**
   - Created a frontend interface to input values and predict salary.

---

## 📊 Model Performance

| Model              | RMSE    | R² Score |
|-------------------|---------|----------|
| Linear Regression | ~10,098 | 0.36     |
| Random Forest     | ~9,351  | 0.46     |

---

## 🚀 How to Run the Project

### 🔧 Local Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/salary-predictor.git
   cd salary-predictor
````

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the Streamlit app:

   ```bash
   streamlit run app.py
   ```

---

## 📈 Future Improvements

* Integrate additional features (e.g., years of experience).
* Use real salary data instead of binary income class mapping.
* Explore advanced models like XGBoost or LightGBM.
* Deploy the app on a cloud platform (e.g., Streamlit Cloud or Heroku).

---

## 📄 License

This project is licensed under the MIT License.

---

## 🙋‍♂️ Author

Aman N Shah
*Passionate about data science and machine learning applications in real-world scenarios.*



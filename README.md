# 🏥 Predictive Patient Readmission Dashboard
**Identifying High-Risk Patients using Machine Learning & SQL**

[![Python](https://img.shields.io/badge/Python-3.13-blue.svg)](https://www.python.org/)
[![Scikit-Learn](https://img.shields.io/badge/Machine%20Learning-Scikit--Learn-orange.svg)](https://scikit-learn.org/)
[![MySQL](https://img.shields.io/badge/Database-MySQL-blue.svg)](https://www.mysql.com/)

## 📝 Project Overview
In the era of Value-Based Care, the **Hospital Readmissions Reduction Program (HRRP)** penalizes hospitals with higher-than-expected 30-day readmission rates. As a clinician, I developed this project to demonstrate how data science can be used for **Risk Stratification** to prevent these readmissions.

This project builds a predictive pipeline that extracts clinical data from a MySQL database and uses a **Random Forest Classifier** to predict which patients are at high risk of being readmitted within 30 days of discharge.

---

## 🚀 The Data Pipeline

### 1. Data Engineering (`database_and_simulation.py`)
- **Simulation Logic:** Developed a synthetic dataset of 1,000 patient encounters. 
- **Clinical Variables:** Includes Age, Primary Diagnosis (CHF, COPD, Sepsis, etc.), Comorbidities, and Length of Stay (LOS).
- **Relational Storage:** The script automatically initializes a MySQL database (`clinical_analytics_db`) and handles secure ETL (Extract, Transform, Load) processes.

### 2. Machine Learning Workflow (`readmission_analysis.py`)
- **Feature Engineering:** Utilized One-Hot Encoding for categorical diagnosis data.
- **Model Selection:** Implemented a **Random Forest Classifier** to handle non-linear clinical relationships.
- **Evaluation Metrics:** Focused on **AUC-ROC** and **Recall**—crucial metrics in healthcare where missing a high-risk patient is more costly than a false alarm.

---

## 📊 Model Performance & Insights
The model evaluates factors that drive patient returns. By analyzing the "Feature Importance," the dashboard provides actionable insights for Discharge Planners.



### Key Metrics Sample:
| Metric | Score | Clinical Interpretation |
| :--- | :--- | :--- |
| **AUC-ROC** | `0.78` | Good ability to distinguish between high and low-risk patients. |
| **Recall (1)** | `0.82` | Successfully identified 82% of patients who were eventually readmitted. |
| **Top Predictor** | `Age` | Strongest correlation with post-discharge complications. |

---

## 📂 Project Structure
```text
├── .env                       # Environment variables (Credentials)
├── .gitignore                 # Securely hides sensitive files
├── requirements.txt           # Project dependencies
├── database_and_simulation.py # ETL: Populates MySQL database
├── readmission_analysis.py    # ML: Trains model and generates report
└── readmission_features.png   # Visualization of risk drivers
```

---

### ⚙️ Installation & Usage 
1. Clone this repository and navigate to the project 
```bash
git clone [https://github.com/azucena-m/predictive-patient-readmission-dashboard.git]
```
2. Setup Credentials: Create a .env file and add your MySQL details:
DB_USER=root
DB_PASSWORD=your_password
DB_HOST=127.0.0.1
DB_NAME=clinical_analytics_db

3. Install dependencies 
pip install -r requirements.txt

4. Execute Pipeline
* First, populate the database: python database_and_simulation.py
* Second, run the analysis: python readmission_analysis.py

---

## Clinical Relevance
This project addresses the "data-to-bedside" gap by identifying high-risk patients before they leave the hospital, Case Managers can prioritize them for:
* Home Health follow-ups
* Telehealth monitoring
* Post-discharge planning

**Author:** Azucena Marroquin - Nurse & Programmer Analyst


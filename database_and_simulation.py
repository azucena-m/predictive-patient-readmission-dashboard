from dotenv import load_dotenv
import os
import pandas as pd
import numpy as np
from faker import Faker
from sqlalchemy import create_engine, text
import urllib.parse
import random

# Database connetion
load_dotenv()
USER = os.getenv('DB_USER')
PASSWORD = os.getenv('DB_PASSWORD')
HOST = os.getenv('DB_HOST')
DATABASE = os.getenv('DB_NAME')
safe_password = urllib.parse.quote_plus(PASSWORD)

# Connect and Create a Database
base_engine = create_engine(f'mysql+pymysql://{USER}:{safe_password}@{HOST}/')
with base_engine.connect() as conn:
    conn.execute(text(f"CREATE DATABASE IF NOT EXISTS {DATABASE}"))

engine = create_engine(f'mysql+pymysql://{USER}:{safe_password}@{HOST}/{DATABASE}')

# ---DATA SIMULATION--- ("Nurse" Logic)
fake = Faker()
patients = []

for p_id in range(1000): #1,000 patients
    age = np.random.randint(18, 90)
    comorbidities = np.random.randint(0, 6)

    #Simulation Logic: High risk if elderly + high comorbidities
    #this creates a signal for the Machine Lerning to find later
    base_risk = 0.05 + (0.1 if age > 65 else 0) + (0.05 * comorbidities)
    readmitted = 1 if np.random.random() < base_risk else 0

    patients.append({
        'patient_id': p_id,
        'age': age,
        'comorbidities_count': comorbidities,
        'primary_diagnosis': random.choice(['CHF', 'COPD', 'Pneumonia', 'Sepsis', 'Diabetes']),
        'length_of_stay': np.random.randint(2, 12),
        'readmitted_within_30d': readmitted #our Target variable
    })

df_patients = pd.DataFrame(patients)

# Push to MySql
df_patients.to_sql('patient_admissions', con=engine, if_exists='replace', index=False)
print("Clinical data was simulated and pusehd to MySql")
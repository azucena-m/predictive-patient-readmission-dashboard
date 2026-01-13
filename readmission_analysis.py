import pandas as pd
import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
import urllib.parse
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, roc_auc_score
import matplotlib.pyplot as plt
import seaborn as sns

# LOAD DATA FROM MYSQL
load_dotenv()
USER, PASSWORD = os.getenv('DB_USER'), os.getenv('DB_PASSWORD')
HOST, DATABASE = os.getenv('DB_HOST'), os.getenv('DB_NAME')
safe_password = urllib.parse.quote_plus(PASSWORD)
engine = create_engine(f'mysql+pymysql://{USER}:{safe_password}@{HOST}/{DATABASE}')

df = pd.read_sql("SELECT * FROM patient_admissions", con=engine)

# PRE-PROCESSIN (Encoding)
# Machine Learning models cannot read "CHF" or "COPD", we convert them into columns of 0s and 1s (One-Hot Encoding)
df_encoded = pd.get_dummies(df, columns=['primary_diagnosis'])

# Define Features (X) and Target (y)
X = df_encoded.drop(['patient_id', 'readmitted_within_30d'], axis=1)
y = df_encoded['readmitted_within_30d']

# TRAIN/TEST SPLIT
# We use 80% to train and 20% to test the model's accuracy
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# MODEL TRAINING
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# EVALUATION
predictions = model.predict(X_test)
probs = model.predict_proba(X_test)[:, 1]

print("--- Model Performance Report ---")
print(classification_report(y_test, predictions))
print(f"Area Under Curve (AUC) Score: {roc_auc_score(y_test, probs):.2f}")

# FEATURE IMPORTANCE VISUALIZATION
# Shows which factors drive readmissions the most
importances = pd.Series(model.feature_importances_, index=X.columns)
importances.nlargest(5).plot(kind='barh', color='teal')
plt.title('Top 5 Predictors of 30-Day Readmissions')
plt.xlabel('Importance Score')
plt.tight_layout()
plt.savefig('readmission_features.png')
plt.show()


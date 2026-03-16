import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
import joblib

# Load dataset
data = pd.read_excel("data/pocso_cases.xlsx")

# Combine facts columns (modify if needed)
data["facts"] = data.astype(str).agg(" ".join, axis=1)

# Labels (you must ensure these columns exist)
sections = data["section"]
outcomes = data["outcome"]

vectorizer = TfidfVectorizer()

X = vectorizer.fit_transform(data["facts"])

section_model = RandomForestClassifier()
section_model.fit(X, sections)

outcome_model = RandomForestClassifier()
outcome_model.fit(X, outcomes)

joblib.dump(section_model, "model/section_model.pkl")
joblib.dump(outcome_model, "model/outcome_model.pkl")
joblib.dump(vectorizer, "model/vectorizer.pkl")

print("Model training complete")

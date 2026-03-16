import joblib

section_model = joblib.load("model/section_model.pkl")
outcome_model = joblib.load("model/outcome_model.pkl")
vectorizer = joblib.load("model/vectorizer.pkl")

def predict_case(facts):

    X = vectorizer.transform([facts])

    section = section_model.predict(X)[0]
    outcome = outcome_model.predict(X)[0]

    reasons = []

    text = facts.lower()

    if "penetration" in text:
        reasons.append("Facts suggest penetration")

    if "medical" in text:
        reasons.append("Medical evidence mentioned")

    if "delay" in text:
        reasons.append("Delay in FIR may affect prosecution")

    if "contradiction" in text:
        reasons.append("Contradictions in testimony")

    return section, outcome, reasons

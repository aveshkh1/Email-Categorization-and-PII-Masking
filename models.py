import joblib

MODEL_PATH = "random_forest_model.pkl"
VECTORIZER_PATH = "tfidf_vectorizer.pkl"

# Map numeric predictions to human-readable labels
LABELS_MAP = {
    0: "Incident",
    1: "Request",
    2: "Problem",
    3: "Change"
}



def predict_category(text):
    model = joblib.load(MODEL_PATH)
    vectorizer = joblib.load(VECTORIZER_PATH)
    X = vectorizer.transform([text])
    predicted = model.predict(X)[0]

    # ✅ Convert label number to category name
    return LABELS_MAP.get(predicted, str(predicted))


from sklearn.pipeline import make_pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import joblib

from src.main import main

def train_and_save():
    X, y = main(path="./data/messages.csv")

    model = make_pipeline(
        TfidfVectorizer(),
        LogisticRegression(max_iter=1000)
    )

    model.fit(X, y)

    joblib.dump(model, "spam_model.pkl")

    print("Model saved successfully.")
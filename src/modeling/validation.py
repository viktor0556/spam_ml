from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.pipeline import make_pipeline
from src.main import main

path="./data/messages.csv"

X, y = main(path)

model = make_pipeline(
    TfidfVectorizer(),
    LogisticRegression(max_iter=1000)
)

scores = cross_val_score(model, X, y, cv=5) # type: ignore

print("Cross-validation scores:", scores)
print("Average accuracy:", scores.mean()) 
""" 
Arra való hogy kiértékelje többféle tesztből az átlagot.
van 5 féle kísérlet:
Fold 1 → [TEST] [TRAIN TRAIN TRAIN TRAIN]
Fold 2 → [TRAIN] [TEST TRAIN TRAIN TRAIN]
Fold 3 → [TRAIN TRAIN] [TEST TRAIN TRAIN]
Fold 4 → [TRAIN TRAIN TRAIN] [TEST TRAIN]
Fold 5 → [TRAIN TRAIN TRAIN TRAIN] [TEST]
Mindegyik eshetőséget megnézi és abból csinál átlaogot.
Ez arra való hogy ne az legyen hogy pont egy szerencsés split miatt
kapjon magas eredményt, ezért minden eshetőséget kipróbál és abból átlagol
"""
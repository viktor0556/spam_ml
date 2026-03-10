from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.pipeline import make_pipeline
from src.main import main
from sklearn.metrics import recall_score, make_scorer, precision_score

path="./messages_data/messages.csv"

X, y = main(path)

model = make_pipeline(
    TfidfVectorizer(),
    LogisticRegression(max_iter=1000)
)

scores = cross_val_score(model, X, y, cv=5) # type: ignore

recall_scorer = make_scorer(recall_score, pos_label="spam")
recall_scores = cross_val_score(model, X, y, cv=5, scoring=recall_scorer) # type: ignore

precision_scorer = make_scorer(precision_score, pos_label="spam")
precision_scores = cross_val_score(model, X, y, cv=5, scoring=precision_scorer) # type: ignore

print("CV scores:", scores)
print("CV recall scores:", recall_scores)
print("CV precision scores:", precision_scores)
# Cross-validation scores: [0.96610169 0.96610169 1.         0.98275862 1.        ]
# Ez a foldot jelöli hogy melyik foldban milyen pontos volt
print(f"Average accuracy:, {scores.mean()}\nAverage recall: {recall_scores.mean()}\nPrecision score: {precision_scores.mean()}") 
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
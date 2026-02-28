from sklearn.linear_model import LogisticRegression
from src.data.splitter import data_split
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
from sklearn.feature_extraction.text import TfidfVectorizer

def clfModel():
  X_train, X_test, y_train, y_test = data_split()
  
  clf = LogisticRegression(max_iter=42)
  
  vectorizer = TfidfVectorizer()

  X_train_vec = vectorizer.fit_transform(X_train) 
  # Megtanulja a szótárat, átalakítja az összes üzenetet számsorrá
  # Eddig kezi featurekben visszaadtunk word_count, char_count stb...
  # Most minden szóhoz hozzárendel egy számot 0 vagy 1
  # "Ma nyaraltam ingyen a fürdőben, nyertem lottón" átalakítja -> 
  # [0, 0, 1, 0, 0, 1, 0] itt az ingyen és lottó volt beállítva spam-nek.
  X_test_vec = vectorizer.transform(X_test)
  # y_pred = clf.predict(X_test) # Megpróbálja az X_test-hez tartozó label-t kitalálni
  
  clf.fit(X_train_vec, y_train)
  y_pred = clf.predict(X_test_vec)
  total = 0
  for pred, true in zip(y_pred, y_test):
    if pred == true:
        total += 1
  
  accuracy = (total / len(y_test)) * 100
  
  cm = confusion_matrix(y_test, y_pred)
  print("Confusion matrix:")
  print(cm)
  
  """          Predicted
           ham   spam
  Actual
  ham      45     5
  spam     10    20
  45 igazi ham amit jól tippelt 5-öt elrontott spamnak jósolta
  10 db volt spam amit rosszul tippelt hamnek, 20 spam volt és 20-at jól tippelt a spamra """
    
  print(classification_report(y_test, y_pred))
  
  """                precision    recall  f1-score   support
  (precision: mennyi volt tényleg spam vagy ham) 
  (recall: Az összes való spam közül mennyit talált meg?)
  (f1-score: precision és recall egyensúlya)
          ham       0.61      0.77      0.68        44         
          spam       0.69      0.50      0.58        44

      accuracy                           0.64        88
    macro avg       0.65      0.64      0.63        88
  weighted avg       0.65      0.64      0.63        88 """
  
  return round(accuracy, 2)

if __name__ == "__main__":
  print(clfModel())
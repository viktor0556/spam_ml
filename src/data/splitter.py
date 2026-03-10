from sklearn.model_selection import train_test_split
from src.main import main
path='./messages_data/messages.csv'

def data_split():
  X, y = main(path)
  from collections import Counter
  X_train, X_test, y_train, y_test = train_test_split(
    X, y, 
    test_size=0.3, stratify=y,
    random_state=42
    )
  print(Counter(y))
  return X_train, X_test, y_train, y_test

if __name__ == "__main__":
  data_split()
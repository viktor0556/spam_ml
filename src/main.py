from src.data.data_loader import load_messages
from typing import Tuple, List

def main(path: str) -> Tuple[List[str], List[str]]:
  messages = load_messages(path)
  
  X = [] # Amit a modell lát
  y = [] # Elvárt kimenet
  #   X → a feature-ök, a bemenet, amit a modell lát
  # y → a label, a kimenet, amit a modellnek meg kell tanulnia
    
  for i in messages:
    features = i['text']
    X.append(features)
    y.append(i['label'])
    
  return X, y

# print(main("./messages_data/messages.csv"))
from src.modeling.train_and_save import train_and_save
from src.cli.predict import prediction
import sys

if __name__ == "__main__":
    command = sys.argv[1]

    if command == "train":
        train_and_save()

    elif command == "predict":
        prediction()

    else:
        print("Usage: python run.py [train|predict]")
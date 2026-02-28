import joblib

def prediction():
    model = joblib.load("./models/spam_model.pkl")
    text = str

    while True:
        text = input("Enter message: ")
        prediction = model.predict([text])
        print("Prediction:", prediction[0])
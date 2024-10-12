import pickle

with open('emails/phishing_email.pkl','rb') as model_file:
    model = pickle.load(model_file)

with open('emails/vectorizer.pkl','rb') as vectorizer_file:
    vectorizer = pickle.load(vectorizer_file)

def predict_email(email_text):
    features = vectorizer.transform([email_text])
    prediction = model.predict(features)
    return prediction[0]
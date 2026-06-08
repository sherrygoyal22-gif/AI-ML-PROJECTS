
import pandas as pd

data = pd.read_csv("spam.csv")

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
X = data["Message"]
y = data["Label"]
  

vectorizer = CountVectorizer()

X_vectorized = vectorizer.fit_transform(X)

model = MultinomialNB()

model.fit(X_vectorized, y)

print("Model Trained Successfully")

message = input("Enter Message: ")

message_vectorized = vectorizer.transform([message])

prediction = model.predict(message_vectorized)

print("Prediction:", prediction[0])
import pandas as pd
from sklearn.linear_model import LinearRegression

data = pd.read_csv("house.csv")

X = data[["Area"]]
y = data["Price"]

model = LinearRegression()

model.fit(X, y)

area = float(input("Enter House Area: "))

prediction = model.predict([[area]])

print("Predicted Price:", prediction[0])
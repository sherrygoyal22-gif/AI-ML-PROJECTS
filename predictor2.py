import pandas as pd
from sklearn.linear_model import LinearRegression

data = pd.read_csv("study_data.csv")

print(data)

X = data[["Hours"]]
y = data["Marks"]

print(X)
print(y)

from sklearn.linear_model import LinearRegression

model = LinearRegression()

model.fit(X, y)

print("Model trained successfully")

prediction = model.predict([[7]])

print(prediction)

hours = float(input("Enter study hours: "))
output = model.predict([[hours]])
print("Output:",output[0])


data = pd.read_csv("salary.csv")

print(data)

X = data[["Experience"]]
y = data["Salary"]

print(X)
print(y)

from sklearn.linear_model import LinearRegression

model = LinearRegression()

model.fit(X, y)

print("Model trained successfully")

prediction = model.predict([[9]])

print(prediction)


exp = float(input("Enter experience years: "))
output = model.predict([[exp]])
print("Output:",output[0])

predictions = model.predict([[7], [8], [10]])
print(predictions[1])





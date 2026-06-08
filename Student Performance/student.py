import pandas as pd
from sklearn.linear_model import LinearRegression
data = pd.read_csv("student.csv")
print(data)

X = data[["Hours", "Attendance"]]
y = data["Marks"]
 
model = LinearRegression()

model.fit(X, y)

prediction = model.predict([[8, 90]])
print(prediction)

hours = float(input("Enter Study Hours: "))
attendance = float(input("Enter Attendance: "))

prediction = model.predict([[hours, attendance]])

print("Predicted Marks:", prediction[0])
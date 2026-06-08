
import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv("marks.csv")
plt.bar(data["Subject"], data["Marks"])

plt.title("student marks dashboard")
plt.xlabel("Subject")
plt.ylabel("Marks")
plt.show()


plt.figure()
data = pd.read_csv("study_data.csv")
plt.bar(data["Hours"], data["Marks"])

plt.title("hours marks dashboard")
plt.xlabel("Hours")
plt.ylabel("Marks")
plt.show()

plt.figure()
data = pd.read_csv("marks.csv")
plt.bar(data["Subject"], data["Marks"])

plt.figure()
plt.plot(data["Subject"], data["Marks"])
plt.show()

plt.figure()
data = pd.read_csv("marks.csv")
plt.bar(data["Subject"], data["Marks"])

plt.figure()
plt.pie(data["Marks"], labels=data["Subject"])
plt.show()

plt.figure()
data = pd.read_csv("marks.csv")
plt.bar(data["Subject"], data["Marks"])

plt.figure()
plt.scatter(data["Marks"], data["Marks"])
plt.show()

plt.figure()
data = pd.read_csv("study_data.csv")
plt.bar(data["Hours"], data["Marks"])

plt.figure()
plt.pie(data["Marks"], labels=data["Hours"])
plt.title("Marks Distribution")
plt.show()
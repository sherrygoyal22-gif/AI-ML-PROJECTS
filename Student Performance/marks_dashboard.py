import pandas as pd
  
data = pd.read_csv("marks.csv")
print(data)
 
print(data["Marks"])
data["Marks"]
print("topper marks:",data["Marks"].max())
print(data["Marks"].min())
print(data["Marks"].sum())
print(data["Marks"].mean())

import pandas as pd
  
data = pd.read_csv("study_data.csv")
print(data)

input("Press Enter to exit...")
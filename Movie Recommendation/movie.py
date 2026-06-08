import pandas as pd

data = pd.read_csv("movies.csv")

print(data)

genre = input("Enter Genre: ")

movies = data[data["Genre"] == genre]

print(movies)

print(movies["Movie"])

print("Recommended Movies:")

for movie in movies["Movie"]:
    print("-", movie)
if movies.empty:
    print("No movies found")
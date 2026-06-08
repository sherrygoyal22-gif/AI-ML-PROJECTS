tasks = ["Practice ML"]
for i in range(3):
 task = input("Enter Task: ")

 tasks.append(task)

print(tasks)

print("Your Tasks:")

for task in tasks:
    print(task)


tasks.remove("Practice ML")
print(tasks)
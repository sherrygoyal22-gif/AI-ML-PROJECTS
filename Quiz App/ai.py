marks = []

for i in range(5):
    mark = int(input("enter mark:"))

    if mark > 0:
        marks.append(mark)

    else:
        print("invalid marks")
          
print( "marks:",marks)

print("highest:", max(marks))
print("lowest:", min(marks))
print("average:", sum(marks)/len(marks))

if mark >= 90:
   print("Grade A" )

elif mark >= 70:
    print("Grade B")

elif mark >= 50:
    print("Grade C")

else:
    print("Fail")

students = {}

for i in range(3):

  name = input("enter name:")

  mark = int(input("enter mark:"))


  students[name] = mark

print(students)
for name, marks in students.items():
 print(name, "=", marks)

students = {
    "Sherry": 85,
    "Aman": 90,
    "Riya": 78
}

search = input("Enter student name: ")

if search in students:
    print("Student found")
else:
    print("Student not found")

search = "Sherry"
print(search,"scored", students[search],"marks")
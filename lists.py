students = ["Miriam", "Ian", "Alex"]
print(students[0])
#replacing an item on the list since the are mutable
students[0] = "Kelvin"
print(students)
#To add an item o the list(At the end f the list)
students.append("Liam")
print(students)
#to insert an item at a specific position in the list
students.insert(1, "Claire")
print(students)
#replacing an item but you don't know the index just the name
if "Ian" in students:
    #finding the index first
    index = students.index("Ian")
    #then we replace with a new item
    students[index] = "Mark"
    print(students)
#replacing mutliple items once
students[2:4] = ("Len", "King")
print(students)
students.pop(1)
print(students)
for student in students:
    print(student)
if "King" in students:
    print("King is a student here")
else:
    print("Not a student here")
print(len(students))

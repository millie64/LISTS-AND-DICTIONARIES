students = [
     {"name":"claire", "age":"20", "sport":"football"},
     {"name":"John", "age":"22", "sport":"volleyball"},
     {"name":"clain", "age":"23", "sport":"soccer"}
]
for student in students:
    print(student["name"], student["sport"], sep=", ")
students.append({"name":"Miriam", "age":"21", "sport":"swimming"})
print(students)
for s in students:
    if s["name"] == "Miriam":
        print("Miriam is",s["age"])
    else:
        print("Miriam is not in the list")
    break

student = {"name":"Sarah", "age":"22", "course":"Computer science"}
student["age"] = "23"
student["grade"] = "A"
del student["course"]
print(student)

fruits = ["orange", "kiwi", "bananas", "melon", "guava"]
fruits[1] = "mango"
fruits.append("pineapple")
fruits.pop(4)
print(fruits)
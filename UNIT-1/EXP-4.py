student = {"name": "Rakesh", "division": 15, "age": 19}
print(student)

print(student["name"])

student["division"] = 15
student["city"] = "Pune"
print(student)

del student["age"]
print(student)

more_info = {"sport": "Football", "hobby": "Watch Movies"}
student.update(more_info)
print(student)
import json

student = {

    "name":"John",
    "age":20,
    "course":"Python"
}

with open(r"C:\Users\Ishit\PycharmProjects\PythonProject7\Week3\Data\student.json","w") as file:
    json.dump(student,file,indent=4)

print("JSON Created")
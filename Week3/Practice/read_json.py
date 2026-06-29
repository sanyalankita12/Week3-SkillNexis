import json

with open(r"C:\Users\Ishit\PycharmProjects\PythonProject7\Week3\Data\student.json","r") as file:
    data=json.load(file)

print(data)
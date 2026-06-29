with open(r"C:\Users\Ishit\PycharmProjects\PythonProject7\Week3\Data\file1.txt", "r") as f1, open(r"C:\Users\Ishit\PycharmProjects\PythonProject7\Week3\Data\file2.txt", "r") as f2:

    data1 = f1.read()
    data2 = f2.read()

with open("merged.txt", "w") as output:
    output.write(data1)
    output.write("\n")
    output.write(data2)

print("Merged Successfully")
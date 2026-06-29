import pandas as pd

df = pd.read_csv(r"C:\Users\Ishit\PycharmProjects\PythonProject7\Week3\Data\data.csv")

# To display the whole dataframe
def display():
    print("\n========== STUDENT DATA ==========\n")
    print(df)
    print("\n==================================\n")

# To display columns
def display_columns():
    print("\n========== COLUMNS ==========")
    print(df.columns)
    print("=============================\n")

# To show average marks
def display_avg():
    print("\n========== AVERAGE MARKS ==========")
    print(f"The Average Marks are: {df['Marks'].mean():.2f}")
    print("===================================\n")

# To show maximum marks
def display_max():
    print("\n========== MAXIMUM MARKS ==========")
    print(f"The Highest Marks are: {df['Marks'].max()}")
    print("===================================\n")

# To show the student with the highest marks
def display_max_student():
    print("\n========== TOPPER DETAILS ==========")
    print("Student(s) with the Highest Marks:")
    print(df[df["Marks"] == df["Marks"].max()])
    print("====================================\n")

display()
display_columns()
display_avg()
display_max()
display_max_student()

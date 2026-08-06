import pandas as pd

data = {
    "Student": ["Aisha", "Ben", "Chen", "Devi", "Ethan", "Farah",
                "Gopal", "Hana", "Ivan", "Jia", "Kumar", "Lina"],
    "StudyHours": [1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0],
    "Attendance": [55, 60, 64, 68, 70, 74, 77, 82, 86, 89, 92, 95],
    "Score": [35, 40, 44, 48, 52, 57, 62, 70, 77, 83, 88, 93]
}

df = pd.DataFrame(data)
print(df)


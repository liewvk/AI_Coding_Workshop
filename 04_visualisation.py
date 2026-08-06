import pandas as pd
import matplotlib.pyplot as plt

data = {
    "StudyHours": [1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0],
    "Score": [35, 40, 44, 48, 52, 57, 62, 70, 77, 83, 88, 93]
}

df = pd.DataFrame(data)

plt.figure(figsize=(8, 5))
plt.scatter(df["StudyHours"], df["Score"])
plt.title("Study Hours and Exam Score")
plt.xlabel("Study Hours")
plt.ylabel("Exam Score")
plt.grid(True)
plt.show()


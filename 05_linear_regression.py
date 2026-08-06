import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error

data = {
    "StudyHours": [1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0],
    "Score": [35, 40, 44, 48, 52, 57, 62, 70, 77, 83, 88, 93]
}

df = pd.DataFrame(data)

X = df[["StudyHours"]]
y = df["Score"]
model = LinearRegression()
model.fit(X, y)

print("Model training completed.")

new_student = pd.DataFrame({"StudyHours": [6.5]})
predicted_score = model.predict(new_student)[0]

print("Predicted score for 6.5 study hours:",
      round(predicted_score, 2))
predicted_scores = model.predict(X)

plt.figure(figsize=(8, 5))
plt.scatter(df["StudyHours"], df["Score"], label="Actual data")
plt.plot(df["StudyHours"], predicted_scores, label="Regression line")
plt.title("Linear Regression: Study Hours vs Score")
plt.xlabel("Study Hours")
plt.ylabel("Score")
plt.grid(True)
plt.legend()
plt.show()

mae = mean_absolute_error(y, predicted_scores)
print("Mean Absolute Error:", round(mae, 2))


import pandas as pd
from sklearn.linear_model import LinearRegression


# -------------------------------------------------
# Step 1: Create the training dataset
# -------------------------------------------------
data = {
    "StudyHours": [
        1.0, 1.5, 2.0, 2.5, 3.0, 3.5,
        4.0, 5.0, 6.0, 7.0, 8.0, 9.0
    ],
    "Score": [
        35, 40, 44, 48, 52, 57,
        62, 70, 77, 83, 88, 93
    ]
}

df = pd.DataFrame(data)


# -------------------------------------------------
# Step 2: Select the feature and label
# -------------------------------------------------
# X contains the input feature.
X = df[["StudyHours"]]

# y contains the value the model learns to predict.
y = df["Score"]


# -------------------------------------------------
# Step 3: Create and train the model
# -------------------------------------------------
model = LinearRegression()
model.fit(X, y)

print("Model training completed.")
print()


# -------------------------------------------------
# Step 4: Enter the study-hour values to predict
# -------------------------------------------------
hours_to_predict = [4.5, 6.5, 8.5]

new_students = pd.DataFrame({
    "StudyHours": hours_to_predict
})


# -------------------------------------------------
# Step 5: Make predictions
# -------------------------------------------------
predictions = model.predict(new_students)


# -------------------------------------------------
# Step 6: Display likely pass or fail results
# -------------------------------------------------
print("STUDENT SCORE PREDICTIONS")
print("-------------------------")

for hours, score in zip(hours_to_predict, predictions):

    if score >= 50:
        result = "Likely Pass"
    else:
        result = "Likely Fail"

    print(
        "Study hours:", hours,
        "| Predicted score:", round(score, 2),
        "|", result
    )


# -------------------------------------------------
# Step 7: Display an important reminder
# -------------------------------------------------
print()
print("Reminder: These predictions are estimates based")
print("on a small demonstration dataset.")


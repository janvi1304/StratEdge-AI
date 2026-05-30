import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder

import pickle


# =========================
# LOAD DATASET
# =========================

df = pd.read_csv("american_bankruptcy.csv")


# =========================
# ENCODE LABELS
# =========================

encoder = LabelEncoder()

df["status_label"] = encoder.fit_transform(
    df["status_label"]
)

# alive = 0
# bankrupt = 1


# =========================
# FEATURES
# =========================

X = df[[

    "X1",
    "X2",
    "X3",
    "X4",
    "X5",
    "X6",
    "X7",
    "X8",
    "X9",
    "X10",
    "X11",
    "X12",
    "X13",
    "X14",
    "X15",
    "X16",
    "X17",
    "X18"

]]


# =========================
# TARGET VARIABLE
# =========================

y = df["status_label"]


# =========================
# TRAIN TEST SPLIT
# =========================

X_train, X_test, y_train, y_test = train_test_split(

    X,
    y,

    test_size=0.2,

    random_state=42

)


# =========================
# CREATE MODEL
# =========================

model = RandomForestClassifier(

    n_estimators=200,

    max_depth=10,

    random_state=42

)


# =========================
# TRAIN MODEL
# =========================

model.fit(X_train, y_train)


# =========================
# MAKE PREDICTIONS
# =========================

predictions = model.predict(X_test)


# =========================
# CHECK ACCURACY
# =========================

accuracy = accuracy_score(

    y_test,

    predictions

)

print("\nBankruptcy Model Accuracy:")
print(round(accuracy * 100, 2), "%")


# =========================
# SAVE MODEL
# =========================

with open("bankruptcy_model.pkl", "wb") as file:

    pickle.dump(model, file)

print("\nBankruptcy model saved successfully.")
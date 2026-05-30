import pandas as pd

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

import pickle


# =========================
# LOAD TRAINING DATA
# =========================

data = pd.read_csv("mna_training_data.csv")


# =========================
# FEATURES
# =========================

X = data[[
    "industry_match",
    "sector_match",
    "market_cap_ratio",
    "cash_ratio"
]]


# =========================
# TARGET VARIABLE
# =========================

y = data["success"]


# =========================
# SPLIT DATA
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

model = RandomForestClassifier()


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

print("\nModel Accuracy:")
print(round(accuracy * 100, 2), "%")


# =========================
# SAVE MODEL
# =========================

with open("mna_model.pkl", "wb") as file:

    pickle.dump(model, file)

print("\nModel saved successfully.")
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import LabelEncoder

def train_model():
    df = pd.read_csv("data/cost_dataset.csv")

    le = LabelEncoder()
    df["Dish"] = le.fit_transform(df["Dish"])

    X = df.drop("Total_Cost", axis=1)
    y = df["Total_Cost"]

    model = LinearRegression()
    model.fit(X, y)

    return model, le


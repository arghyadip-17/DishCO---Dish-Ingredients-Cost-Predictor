import streamlit as st
import pandas as pd
from model.cost_model import train_model

# Load data
ingredient_df = pd.read_csv("data/ingredients_per_person.csv")
model, le = train_model()

st.set_page_config(page_title="DishCO — Predicts Dish Ingredients & Costs", layout="wide")
st.title("🍛 DishCO - Dish Ingredients & Cost Predictor")

dish = st.selectbox("Select Dish", ingredient_df["Dish"].unique())
people = st.number_input("Number of People", 1, 100, 5)

if st.button("Predict"):
    dish_data = ingredient_df[ingredient_df["Dish"] == dish].copy()
    dish_data["Total_Qty"] = dish_data["Qty_per_person"] * people

    st.subheader("🧂 Ingredients Required")
    st.table(dish_data[["Ingredient", "Total_Qty", "Unit"]])

    def get_qty(name):
        return dish_data.loc[dish_data["Ingredient"] == name, "Total_Qty"].sum()

    rice = get_qty("Rice")
    chicken = get_qty("Chicken")
    paneer = get_qty("Paneer")
    lentils = get_qty("Lentils")
    vegetables = get_qty("Vegetables")
    oil = get_qty("Oil")
    spices = get_qty("Spices")

    dish_encoded = le.transform([dish])[0]

    cost = model.predict([[dish_encoded, people, rice, chicken, paneer, lentils, vegetables, oil, spices]])
    st.success(f"💰 Estimated Cost: ₹{int(cost[0])}")

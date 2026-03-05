# 🍛 DishCO – Dish Ingredients & Cost Predictor

DishCO is a simple **Machine Learning + Streamlit** application that predicts the **estimated cost of a dish** based on:
- Selected dish
- Number of people
- Required ingredients and their quantities

It also shows the **ingredients required** dynamically based on the number of people.

---

## 🚀 Features

- 📋 Select a dish from the menu
- 👨‍👩‍👧 Enter number of people
- 🧂 Automatically calculates ingredient quantities
- 🤖 Machine Learning model predicts total cost
- 💰 Cost displayed in Indian Rupees (₹)
- 🌐 Easy-to-use Streamlit web interface

---

## 🛠️ Tech Stack

- **Python**
- **Streamlit** (Web UI)
- **Pandas** (Data handling)
- **Scikit-learn** (ML model)
- **Linear Regression**
- **Label Encoding**


---

## 📊 Dataset Description

### 1️⃣ `ingredients_per_person.csv`
Contains ingredient quantity required **per person** for each dish.

Example columns:
- Dish
- Ingredient
- Qty_per_person
- Unit

### 2️⃣ `cost_dataset.csv`
Used for training the ML model.

Example columns:
- Dish
- People
- Rice
- Chicken
- Paneer
- Lentils
- Vegetables
- Oil
- Spices
- Total_Cost (Target)

---

## 🤖 Machine Learning Model

- **Algorithm:** Linear Regression  
- **Encoding:** LabelEncoder for dish names  
- **Target Variable:** `Total_Cost`

### Model Flow:
1. Load dataset
2. Encode dish names
3. Train Linear Regression model
4. Predict total cost based on inputs

---

## ▶️ Live Website

=> https://dishco-dish-ingredients-cost-predictor-1.onrender.com

<img width="1919" height="893" alt="image" src="https://github.com/user-attachments/assets/54018e28-7311-4e1a-a0ab-dd097321cd91" />

---
## Author
Arghyadip Ghosh

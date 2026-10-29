import streamlit as st
import pandas as pd
import joblib
import numpy as np

model = joblib.load("car_price_model.pkl")
feature_columns = joblib.load("model_features.pkl")

st.title("Ford Car Price Prediction")

model_input = st.selectbox(
    "Model",
    ['Fiesta','Focus','Puma','EcoSport','Kuga','C-MAX','Mondeo','Ka+',
     'Tourneo Custom','S-MAX','B-MAX','Edge','Tourneo Connect',
     'Grand C-MAX','KA','Galaxy','Grand Tourneo Connect','Fusion']
)

year = st.number_input("Year", min_value=1950, max_value=2025, value=2019)

transmission = st.selectbox(
    "Transmission",
    ["Manual", "Semi-Automatic", "Automatic"]
)

mileage = st.number_input("Mileage", min_value=0, value=24)

fuel_type = st.selectbox(
    "Fuel Type",
    ["Petrol", "Diesel", "Hybrid", "Electric"]
)

tax = st.number_input("Tax", min_value=0, value=145)
mpg = st.number_input("MPG", min_value=8.0, value=65.7)
engine_size = st.number_input("Engine Size", min_value=0.6, value=2.0)





if st.button("Predict Price"):
    input_df = pd.DataFrame([{
        "model": model_input,
        "year": year,
        "transmission": transmission,
        "mileage": mileage,
        "fuelType": fuel_type,
        "tax": tax,
        "mpg": mpg,
        "engineSize": engine_size,
    }])

    input_df = pd.get_dummies(
        input_df,
        columns=["model", "fuelType", "transmission"],
        drop_first=True
    )
    
    input_df = input_df.reindex(columns=feature_columns, fill_value=0)

    prediction = np.exp(model.predict(input_df).item())

    st.success(f"Estimated Price: {prediction:,.0f}$")

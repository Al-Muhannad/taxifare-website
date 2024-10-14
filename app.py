import streamlit as st
from datetime import datetime
import requests

st.title("Taxi Fare Prediction")

ride_date = st.date_input("Select the date of the ride", datetime.now().date())
ride_time = st.time_input("Select the time of the ride", datetime.now().time())

ride_datetime = datetime.combine(ride_date, ride_time)
formatted_datetime = ride_datetime.strftime('%Y-%m-%d+%H:%M:%S')

pickup_longitude = st.number_input("Pickup Longitude", format="%.6f")
pickup_latitude = st.number_input("Pickup Latitude", format="%.6f")

dropoff_longitude = st.number_input("Dropoff Longitude", format="%.6f")
dropoff_latitude = st.number_input("Dropoff Latitude", format="%.6f")

passenger_count = st.number_input("Passenger Count", min_value=1, step=1)

url = (
    f'https://taxifare.lewagon.ai/predict?pickup_datetime={formatted_datetime}'
    f'&pickup_longitude={pickup_longitude}&pickup_latitude={pickup_latitude}'
    f'&dropoff_longitude={dropoff_longitude}&dropoff_latitude={dropoff_latitude}'
    f'&passenger_count={passenger_count}'
)

if st.button('Predict Fare'):
        response = requests.get(url)

        if response.status_code == 200:
            prediction = response.json()
            st.write(f"The predicted fare is: ${prediction['fare']}")
        else:
            st.write(f"Error in API call: {response.status_code}")

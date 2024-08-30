import streamlit as st
import datetime
import requests
'''
# TaxiFareModel front
'''

st.markdown('''
Remember that there are several ways to output content into your web page...

Either as with the title by just creating a string (or an f-string). Or as with this paragraph using the st. functions
''')

'''
## Here we would like to add some controllers in order to ask the user to select the parameters of the ride

1. Let's ask for:
- date and time
- pickup longitude
- pickup latitude
- dropoff longitude
- dropoff latitude
- passenger count
'''
import streamlit as st


# Create a title for the app
st.title("Ride Parameters")

# Ask for date and time
pickup_date = st.date_input("Select date:", value=datetime.date.today(), key="pickup_date")
pickup_time = st.time_input("Select time:", value=datetime.datetime.now(), key="pickup_time")

# Ask for pickup location
pickup_longitude = st.number_input("Pickup longitude:", value=40.0, step=0.01, key="pickup_longitude")
pickup_latitude = st.number_input("Pickup latitude:", value=40.0, step=0.01, key="pickup_latitude")

# Ask for dropoff location
dropoff_longitude = st.number_input("Dropoff longitude:", value=40.0 , step=0.01, key="dropoff_longitude")
dropoff_latitude = st.number_input("Dropoff latitude:", value=40.0, step=0.01, key="dropoff_latitude")

# Ask for passenger count
passenger_count = st.number_input("Number of passengers:", value=1, step=1, key="passenger_count")

# Display the input values
st.write("You selected:")
st.write(f"Date and time: {pickup_date} {pickup_time}")
st.write(f"Pickup location: ({pickup_longitude}, {pickup_latitude})")
st.write(f"Dropoff location: ({dropoff_longitude}, {dropoff_latitude})")
st.write(f"Number of passengers: {passenger_count}")

'''
## Once we have these, let's call our API in order to retrieve a prediction

See ? No need to load a model.joblib file in this app, we do not even need to know anything about Data Science in order to retrieve a prediction...

🤔 How could we call our API ? Off course... The requests package 💡
'''

url = 'https://taxifare.lewagon.ai/predict'

if url == 'https://taxifare.lewagon.ai/predict':

    st.markdown('Maybe you want to use your own API for the prediction, not the one provided by Le Wagon...')

'''

2. Let's build a dictionary containing the parameters for our API...

3. Let's call our API using the requests package...

4. Let's retrieve the prediction from the *JSON* returned by the API...

## Finally, we can display the prediction to the user
'''
params = {
    "pickup_datetime": f"{pickup_date} {pickup_time}",
    "pickup_longitude": pickup_longitude,
    "pickup_latitude": pickup_latitude,
    "dropoff_longitude": dropoff_longitude,
    "dropoff_latitude": dropoff_latitude,
    "passenger_count": passenger_count
}

response = requests.get("https://taxifare.lewagon.ai/predict", params=params)


if response.status_code == 200:

    prediction = response.json()["fare"]
    st.write("Prediction:", prediction)
else:
    st.write("Error:", response.status_code)

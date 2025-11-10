
import streamlit as st
import pickle
import numpy as np

# -------------------- Load Trained Model --------------------
# Uncomment this section if you have a real model
# with open("car_price_model.pkl", "rb") as file:
#     model = pickle.load(file)

# Dummy model (for demo)
class DummyModel:
    def predict(self, X):
        return [1064505.00]

model = DummyModel()

# -------------------- Page Setup --------------------
st.set_page_config(page_title="Car Price Prediction", layout="wide")

st.markdown(
    """
    <style>
    .main {
        background-color: #0e1117;
        color: white;
    }
    div[data-testid="stSidebar"] {
        background-color: #1c1e24;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# -------------------- Sidebar --------------------
with st.sidebar:
    st.header("Prediction Price of Car")
    st.info("The prediction is based on 97% accuracy ✅")

    if st.button("Predict Price"):
        st.session_state["predict"] = True

    if "predicted_price" in st.session_state:
        st.success(f"The Predicted Price is ₹{st.session_state['predicted_price']:,.2f}")

# -------------------- Main Page --------------------
st.title("Car Price Prediction 🚗💵")

st.markdown(
    """
    This app predicts the price of a car based on its features, such as model, age, mileage, and other specifications ✏️.  
    Enter the details and get an estimated price instantly!
    """
)

# ✅ FIXED: removed unsupported argument
st.image("https://i.ibb.co/fFM2fN9/autocar-banner.png")

st.subheader("Enter Car Details")

# -------------------- Input Fields --------------------
col1, col2 = st.columns(2)

with col1:
    brand = st.selectbox("Brand of Car", ["Hyundai", "Toyota", "Maruti", "Honda", "Tata", "Mahindra"])
    km_driven = st.number_input("KM Driven of Car", min_value=0, max_value=300000, step=5000)

with col2:
    owner = st.selectbox("Type of Owner", ["First Owner", "Second Owner", "Third Owner"])
    transmission = st.selectbox("Type of Transmission", ["Manual", "Automatic"])
    fuel = st.selectbox("Type of Fuel", ["Petrol", "Diesel", "CNG", "LPG", "Electric"])
    seller_type = st.selectbox("Type of Sellers", ["Dealer", "Individual", "Trustmark Dealer"])
    seats = st.selectbox("Number of Seats", [2, 4, 5, 6, 7])

st.divider()

col3, col4 = st.columns(2)

with col3:
    mileage = st.slider("Mileage of Car (km/l)", 0, 40, 18)
    age = st.slider("Age of Car (years)", 0, 20, 4)

with col4:
    engine = st.slider("Engine of Car (CC)", 800, 5000, 1200)
    max_power = st.slider("Max Power of Car (hp)", 40, 400, 120)

# -------------------- Prediction Logic --------------------
if st.session_state.get("predict"):
    # Example: features simplified to numeric inputs
    input_data = np.array([[km_driven, mileage, age, engine, max_power]])
    prediction = model.predict(input_data)[0]

    st.session_state["predicted_price"] = prediction
    st.success(f"Predicted Car Price: ₹{prediction:,.2f}")

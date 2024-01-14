import streamlit as st
import math
# from PIL import GifImagePlugin, Image, ImageFile
import matplotlib

# Set the backend to 'macosx' explicitly
matplotlib.use('macosx')

import streamlit as st
import math
from PIL import Image
def calculate_emi(principal, interest_rate, tenure):
    interest_rate = interest_rate / 12 / 100
    emi = principal * interest_rate * math.pow(1 + interest_rate, tenure) / (math.pow(1 + interest_rate, tenure) - 1)
    return emi

def main():
    st.title("Home Loan EMI Calculator")

    principal = st.number_input("Loan Amount (in lakh INR)", min_value=1) * 100000
    interest_rate = st.number_input("Interest Rate (%)", min_value=0.1, max_value=20.0, step=0.1)
    tenure_years = st.number_input("Loan Tenure (Years)", min_value=1, max_value=50)

    tenure_months = tenure_years * 12

    if st.button("Calculate EMI"):
        emi = calculate_emi(principal, interest_rate, tenure_months)
        st.success(f"Your EMI is: ₹{emi:.2f}")

if __name__ == "__main__":
    main()

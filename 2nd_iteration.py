import streamlit as st
import math
import matplotlib.pyplot as plt


def calculate_emi(principal, interest_rate, tenure):
    interest_rate = interest_rate / 12 / 100
    emi = principal * interest_rate * math.pow(1 + interest_rate, tenure) / (math.pow(1 + interest_rate, tenure) - 1)
    return emi


def calculate_amortization_schedule(principal, interest_rate, tenure):
    schedule = []
    remaining_principal = principal

    for month in range(1, tenure + 1):
        interest_payment = remaining_principal * interest_rate / 12 / 100
        principal_payment = calculate_emi(principal, interest_rate, tenure) - interest_payment
        remaining_principal -= principal_payment

        schedule.append((month, interest_payment, principal_payment))

    return schedule


def main():
    st.title("Home Loan EMI Calculator")

    principal = st.number_input("Loan Amount (INR)", min_value=1)
    interest_rate = st.number_input("Interest Rate (%)", min_value=0.1, max_value=20.0, step=0.1)

    use_tenure = st.checkbox("Provide Loan Tenure (Years)")

    if use_tenure:
        tenure_years = st.number_input("Loan Tenure (Years)", min_value=1, max_value=50)
        tenure_months = tenure_years * 12
    else:
        emi = st.number_input("EMI Amount", min_value=1)
        # Calculate the tenure based on the formula for EMI calculation
        tenure_months = math.ceil(
            -(math.log(1 - (principal * interest_rate / 12 / 100) / emi) / math.log(1 + interest_rate / 12 / 100)))
        st.success(f"Calculated Loan Tenure: {tenure_months // 12} years and {tenure_months % 12} months")

    if st.button("Calculate"):
        if use_tenure:
            emi = calculate_emi(principal, interest_rate, tenure_months)
            st.success(f"Your EMI is: ₹{emi:.2f}")

        amortization_schedule = calculate_amortization_schedule(principal, interest_rate, tenure_months)

        # Extracting data for pie chart
        interest_payments = sum(entry[1] for entry in amortization_schedule)
        principal_payments = sum(entry[2] for entry in amortization_schedule)

        # Pie chart
        labels = [f'Interest\n₹{interest_payments:.2f} ({interest_payments / principal * 100:.1f}%)',
                  f'Principal\n₹{principal_payments:.2f} ({principal_payments / principal * 100:.1f}%)']
        sizes = [interest_payments, principal_payments]
        colors = ['#ff9999', '#66b3ff']

        fig1, ax1 = plt.subplots()
        ax1.pie(sizes, labels=labels, autopct='', colors=colors, startangle=90)
        ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

        st.pyplot(fig1)


if __name__ == "__main__":
    main()

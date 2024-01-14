import math

def calculate_emi(principal, interest_rate, tenure):
    interest_rate = interest_rate / 12 / 100
    emi = principal * interest_rate * math.pow(1 + interest_rate, tenure) / (math.pow(1 + interest_rate, tenure) - 1)
    return emi

def main():
    print("Home Loan EMI Calculator")

    principal = float(input("Enter Loan Amount (INR): "))
    interest_rate = float(input("Enter Interest Rate (%): "))
    tenure_years = int(input("Enter Loan Tenure (Years): "))

    tenure_months = tenure_years * 12

    emi = calculate_emi(principal, interest_rate, tenure_months)
    print(f"Your EMI is: ₹{emi:.2f}")

if __name__ == "__main__":
    main()

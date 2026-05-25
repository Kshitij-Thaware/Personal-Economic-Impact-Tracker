import streamlit as st

from api import get_market_data

from analysis import calculate_financial_health

st.set_page_config(page_title = "Economic Impact Dashboard")

st.title("Economic Impact Dashboard")

# Get market data

data = get_market_data()

st.subheader("Live Economic Stats")

col1, col2, col3 = st.columns(3)

col1.metric("NIFTY", data["NIFTY"])
col2.metric("USD/INR", data["USD_INR"])
col3.metric("Gold", data["GOLD"])

st.divider()

# User Input
st.subheader("Personal Financial Health Analysis")

salary = st.number_input("Monthly Salary", min_value = 0)

rent = st.number_input("Monthly Rent", min_value = 0)

emi = st.number_input("Monthly EMI", min_value = 0)

fuel = st.number_input("Monthly Fuel Expense", min_value = 0)

groceries = st.number_input("Monthly Groceries Expense", min_value = 0)

if st.button("Analyze"):

    result = calculate_financial_health(
        salary,
        rent,
        emi,
        fuel,
        groceries
    )

    st.subheader("Your Economic Health Score")

    st.metric("Total Expenses", result["expenses"])

    st.metric("Monthly Savings", result["savings"])

    st.metric("Financial Stress Score", f"{result['stress_score'][0]}%")

    if result["stress_score"][0] > 80:
        st.error("High Financial Stress")

    elif result["stress_score"][0] > 60:
        st.warning("Moderate Financial Stress")

    else:
        st.success("Healthy Financial Condition")
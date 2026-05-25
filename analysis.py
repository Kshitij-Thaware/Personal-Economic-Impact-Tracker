# FIle for analysis of the data collected by the Personal Economic Impact Tracker

def calculate_financial_health(
        salary,
        rent,
        emi,
        fuel,
        groceries
):
    total_expense = rent + eni + fuel + groceries

    savings = salary - total_expense

    stress_score = (total_expense / salary) * 100

    return{
        "expenses": total_expense,
        "savings": savings,
        "stress_score": (stress_score,2)
    }
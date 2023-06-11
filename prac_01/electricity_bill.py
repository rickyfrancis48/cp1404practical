print("Electricity bill estimator")
per_hour_cost = float(input("Enter cents per kWh: "))
daily_use = float(input("Enter daily use in kWh: "))
days_until_bill = float(input("Enter number of billing days: "))
total = (per_hour_cost/100) * daily_use * days_until_bill
print(f"Estimated bill: ${total}")

# Prompt the user for revenue (float) and cost (float)

revenue = float(input("Enter revenue: "))
cost = float(input("Enter cost: "))
profit = revenue - cost

# Calculate profit = revenue - cost

#calulate margin = profit / revenue
# Print the results fomatted nicely, e.g. "Profit: $X.XX | Margin: Y.YY%" round to 2 decimal places

if revenue > 0: 
    margin = ( profit / revenue ) * 100
    profit = revenue - cost

    print(f"Profit: ${profit:.2f} | Margin: {margin:.2f}%")
else:
    print("Revenue must be greater than 0 to calculate margin.")


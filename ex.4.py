def get_tax_bracket(income):
    """
    Determines the tax bracket based on income and returns a formatted string.
    """
    if income < 0:
        return "Invalid income."
    elif income >= 100000:
        bracket = "High (30%)"
    elif income >= 50000:
        bracket = "Medium (20%)"
    else:  
        bracket = "Low (10%)"

    return bracket + (" (Deduction Eligible)" if income % 2 == 0 else "")


try:
    annual_income = float(input("What's your annual income? "))
    bracket_info = get_tax_bracket(annual_income)

    if "Invalid" not in bracket_info:
        if "High" in bracket_info:
            rate = 0.30
        elif "Medium" in bracket_info:
            rate = 0.20
        else:
            rate = 0.10
        
        estimated_tax = annual_income * rate
        print(f"Your bracket: {bracket_info}. Estimated tax: {estimated_tax: .2f}")
    else:
        print(bracket_info)

except ValueError:
    print("Invalid input. Please enter a valid number.")
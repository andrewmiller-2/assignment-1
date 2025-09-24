credit_score = int(input("What is your credit score? "))
if credit_score < 300 or credit_score > 850:
    print("Invalid score.")
elif credit_score >= 750:
    print("Excellent - Loan Approved")
    print("Interest rate: Low")
elif credit_score >= 700:
    print("Good - Loan Approved with Review")
    print("Interest rate: Low")
elif credit_score >= 600:
    print("Fair - Loan Conditional")
    print("Seek credit improvement.")
else:  
    print("Poor - Loan Denied")
    print("Seek credit improvement.")
Valid_payments = ["GCash", "Cash", "Card"]

Payment_method = input("Enter payment method (GCash, Cash, Card): ")

if Payment_method in Valid_payments:
    print("Valid payment method.")

else:
    print("Invalid payment method.")
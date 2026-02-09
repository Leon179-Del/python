premiumrates = float(input("Enter your gross income"))
if premiumrates > 0 and premiumrates <= 5999:
    print("Monthly contribution is 150.00")
elif premiumrates >= 8000 and premiumrates <= 11999:
    print("Monthly contribution is 300.00")
elif premiumrates >= 12000 and premiumrates <= 14999:
    print("Monthly contribution is 400.00")
elif premiumrates >= 15000 and premiumrates <= 19999:
    print("Monthly contribution is 600.00")
elif premiumrates >= 20000 and premiumrates <= 24999:
    print("Monthly contribution is 750.00")
elif premiumrates >= 25000 and premiumrates <= 29999:
    print("Monthly contribution is 850.00")
elif premiumrates >= 30000 and premiumrates <= 49999:
    print("Monthly contribution is 1000.00")
elif premiumrates >= 50000 and premiumrates <= 99999:
    print("Monthly contribution is 1500.00")
elif premiumrates >= 100000:
    print("Monthly contribution is 2000.00")
else:
    print("Invalid input")
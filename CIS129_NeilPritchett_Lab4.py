# Module 4 Lab - Part 4: Full Bonus Calculation Program
# Author: Neil Pritchett
# Date: February 25, 2025
# Description: This program calculates store and employee bonuses based on sales.

# Declare variables
monthlySales = float(input("Enter the monthly sales: "))
storeAmount = 0
empAmount = 0
salesIncrease = 0

# Determine store bonus
if monthlySales >= 110000:
    storeAmount = 6000
elif monthlySales >= 100000:
    storeAmount = 5000
elif monthlySales >= 90000:
    storeAmount = 4000
elif monthlySales >= 80000:
    storeAmount = 3000
else:
    storeAmount = 0

# Get sales increase
salesIncrease = float(input("Enter the percent of sales increase: ")) / 100

# Determine employee bonus
if salesIncrease >= 0.05:
    empAmount = 75
elif salesIncrease >= 0.04:
    empAmount = 50
elif salesIncrease >= 0.03:
    empAmount = 40
else:
    empAmount = 0

# Print results
print("The store bonus amount is $", storeAmount)
print("The employee bonus amount is $", empAmount)

if storeAmount == 6000 and empAmount == 75:
    print("Congrats! You have reached the highest bonus amounts possible!")
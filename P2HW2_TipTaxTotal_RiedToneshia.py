#CTI - 110
#P2HW1-Tip Tax Total
#Toneshia Ried
#February 14, 2018

FoodCost = float(input('Enter the Food Cost:'))
TipAmount = 0.18 * FoodCost
SalesTax = 0.07 * FoodCost
TotalCost = FoodCost + TipAmount + SalesTax
print("Food Charge: $" + format(FoodCost, ",.2f"))
print("Tip Amount: $" + format(TipAmount, ",.2f"))
print("Sales Tax: $" + format(SalesTax, ",.2f"))
print("Total Cost: $" + format(TotalCost, ",.2f"))

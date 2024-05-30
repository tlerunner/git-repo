#Write a program that calculates the total amount of a meal purchased at a restaurant.
#The program should ask the user to enter the charge for the food and then calculate
#the amounts with an 18 percent tip and 7 percent sales tax. Display each of these amounts
#and the total price.

#initialize variables
CONST_tip_rate_per = 18.0
CONST_sales_tax_rate_per = 7.0
food_charge_dollars = 0.0
tip_dollars = 0.0
sales_tax_dollars = 0.0
total_charge_dollars = 0.0

#prompt for food charge and echo back
food_charge_dollars = float(input('Enter the total food charge in dollars and cents (do not include the $): '))
print('\nYou entered: ${:.2f}\n'.format(food_charge_dollars))

#calculate tip
tip_dollars = food_charge_dollars * (CONST_tip_rate_per/100)

#calculate sales tax
sales_tax_dollars = food_charge_dollars * (CONST_sales_tax_rate_per/100)

#calculate total charge
total_charge_dollars = food_charge_dollars + tip_dollars + sales_tax_dollars

#print report
print('Food Charge:   ${:.2f}'.format(food_charge_dollars))
print('Tip:           ${:.2f}'.format(tip_dollars))
print('Sales Tax:     ${:.2f}'.format(sales_tax_dollars))
print('-----------------------')
print('Total:         ${:.2f}\n'.format(total_charge_dollars))
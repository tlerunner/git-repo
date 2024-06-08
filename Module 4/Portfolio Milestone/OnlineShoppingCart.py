# Step 1: Build the ItemToPurchase class with the following specifications:

#   Attributes
#     item_name (string)
#     item_price (float)
#     item_quantity (int)
#   Default constructor
#     Initializes item's name = "none", item's price = 0, item's quantity = 0
#   Method
#     print_item_cost()
#   Example of print_item_cost() output:
#     Bottled Water 10 @ $1 = $10

#   Define ItemsToPurchase class
class ItemsToPurchase:
    item_name = ''
    item_price = 0.0
    item_quantity = 0
    def __init__(self,item_name = 'none',item_price = 0,item_quantity = 0):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity
    def print_item_cost(self):
        print('{} {} @${:.2f} = ${:.2f}'.format(self.item_name,self.item_quantity,self.item_price,self.item_price*self.item_quantity))

#   Example of print_item_cost() output:
#   Bottled Water 10 @ $1 = $10

# Step 2: In the main section of your code, prompt the user for two items and create two objects of the ItemToPurchase class.
#
#   Example:
#     Item 1
#       Enter the item name:
#         Chocolate Chips
#       Enter the item price:
#         3
#       Enter the item quantity:
#         1
#     Item 2
#       Enter the item name:
#         Bottled Water
#       Enter the item price:
#         1
#       Enter the item quantity:
#         10

# Constant which defines the number of items in the shopping cart
number_of_items = 2

# Create shopping cart with the specified number of items
Items = []
for i in range(number_of_items):
    Items.append(ItemsToPurchase())

# Put items in the shopping cart
number = 0
for x in Items:
    print('Item {}'.format(number+1))
    x.item_name = input('Enter the item name:')
    x.item_price = float(input('Enter the item price:'))
    x.item_quantity = int(input('Enter the item quantity:'))
    number += 1

# Step 3: Add the costs of the two items together and output the total cost.
# 
#    Example:
#     TOTAL COST
#       Chocolate Chips 1 @ $3 = $3
#       Bottled Water 10 @ $1 = $10
#       Total: $13

total_cost = 0
number = 0
print('TOTAL COST')
for x in Items:
    x.print_item_cost()
    total_cost = total_cost + x.item_quantity * x.item_price
    number += 1
print('Total: ${:.2f}'.format(total_cost))
        


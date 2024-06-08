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

Item_1 = ItemsToPurchase()
Item_2 = ItemsToPurchase()

print('Item 1')
Item_1.item_name = input('Enter the item name:')
Item_1.item_price = float(input('Enter the item price:'))
Item_1.item_quantity = int(input('Enter the item quantity:'))

print('Item 2')
Item_2.item_name = input('Enter the item name:')
Item_2.item_price = float(input('Enter the item price:'))
Item_2.item_quantity = int(input('Enter the item quantity:'))

# Step 3: Add the costs of the two items together and output the total cost.
# 
#    Example:
#     TOTAL COST
#       Chocolate Chips 1 @ $3 = $3
#       Bottled Water 10 @ $1 = $10
#       Total: $13

print('TOTAL COST')
Item_1.print_item_cost()
Item_2.print_item_cost()
print('Total: ${}'.format(Item_1.item_quantity * Item_1.item_price + Item_2.item_quantity * Item_2.item_price))
        


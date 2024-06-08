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

# Initialize Items list
Items = []

# Initialize Sentinel Character
user_input = ''

# Gather shopping cart entries until the user enters a 'q'
while user_input != 'q':
    Items.append(ItemsToPurchase())
    print('Item {}'.format(len(Items)))
    Items[-1].item_name = input('Enter the item name:')
    Items[-1].item_price = float(input('Enter the item price:'))
    Items[-1].item_quantity = int(input('Enter the item quantity:'))
    user_input = input('Enter q to quit, any other key to add another item.')

# Print out cost of each item and the total cost
total_cost = 0
print('TOTAL COST')
for x in Items:
    x.print_item_cost()
    total_cost = total_cost + x.item_quantity * x.item_price
print('Total: ${:.2f}'.format(total_cost))
        


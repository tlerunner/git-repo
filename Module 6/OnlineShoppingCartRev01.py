#   Define ItemsToPurchase class
class ItemsToPurchase:
    item_name = ''
    item_price = 0.0
    item_quantity = 0
    def __init__(self,item_name = 'none',item_description = 'none',item_price = 0,item_quantity = 0):
        self.item_name = item_name
        self.item_description = item_description
        self.item_price = item_price
        self.item_quantity = item_quantity
    def print_item_cost(self):
        print('{} {} @${:.2f} = ${:.2f}'.format(self.item_name,self.item_quantity,self.item_price,self.item_price*self.item_quantity))

#   Define ShoppingCart class
class ShoppingCart: #Parameterized constructor, which takes the customer name and date as parameters
    customer_name = 'none'
    current_date = 'January 1, 2020'
    def __init__(self,customer_name = 'none',current_date = 'January 1, 2020'):
        self.customer_name = customer_name #customer_name (string) - Initialized in default constructor to "none"
        self.current_date = current_date #current_date (string) - Initialized in default constructor to "January 1, 2020"
        self.cart_items = [] #cart_items (list)
    def add_item(self,ItemsToPurchase): #Adds an item to cart_items list. Has parameter ItemToPurchase. Does not return anything.
        self.cart_items.append(ItemsToPurchase) 
    def remove_item(self,item_name): #Removes item from cart_items list. Has a string (an item's name) parameter. Does not return anything. 
        index = 0
        found = False
        for cart_item in self.cart_items:
            if item_name == cart_item.item_name:
                del self.cart_items[index]
                found = True
                break
            index += 1
        if not found:
            print('Item not found in cart. Nothing removed.') #If item name cannot be found, output this message: Item not found in cart. Nothing removed.
    def modify_item(self,ItemToPurchase): #Modifies an item's description, price, and/or quantity. Has parameter ItemToPurchase. Does not return anything.
        index = 0
        found = False
        temp = ItemsToPurchase()
        for cart_item in self.cart_items:
            if ItemToPurchase.item_name == cart_item.item_name: #If item can be found (by name) in cart,
                if ItemToPurchase.item_description != temp.item_description: #check if parameter has default values for description, price, and quantity.
                    self.cart_items[index].item_description = ItemToPurchase.item_description #If not, modify item in cart
                if ItemToPurchase.item_price != temp.item_price: #check if parameter has default values for description, price, and quantity.
                    self.cart_items[index].item_price = ItemToPurchase.item_price #If not, modify item in cart
                if ItemToPurchase.item_quantity != temp.item_quantity: #check if parameter has default values for description, price, and quantity.
                    self.cart_items[index].item_quantity = ItemToPurchase.item_quantity #If not, modify item in cart
                found = True
                break
            index += 1
        if not found: #If item cannot be found (by name) in cart
            print('Item not found in cart. Nothing modified.')  #output this message: Item not found in cart. Nothing modified.       
    def get_num_items_in_cart(self): #Returns quantity of all items in cart. Has no parameters
        num_items = 0
        for cart_item in self.cart_items:
            num_items = num_items + cart_item.item_quantity
        return num_items
    def get_cost_of_cart(self): #Determines and returns the total cost of items in cart. Has no parameters
        total_cost = 0
        for cart_item in self.cart_items:
            total_cost = total_cost + cart_item.item_price * cart_item.item_quantity
        return total_cost
    def print_total(self): #Outputs total of objects in cart.
        print('OUTPUT SHOPPING CART')
        if self.get_num_items_in_cart() > 0:
            print('{}\'s Shopping Cart - {}'.format(self.customer_name,self.current_date))
            print('Number of Items: {}'.format(self.get_num_items_in_cart()))
            for cart_item in self.cart_items:
                cart_item.print_item_cost()
                print('Total: ${:.2f}'.format(self.get_cost_of_cart()))
        else:
            print('SHOPPING CART IS EMPTY') #If cart is empty, output this message: SHOPPING CART IS EMPTY
    def print_descriptions(self): #Outputs each item's description
        print('OUTPUT ITEMS\'S DESCRIPTIONS')
        print('{}\'s Shopping Cart - {}'.format(self.customer_name,self.current_date))
        for cart_item in self.cart_items:
            print('{}: {}'.format(cart_item.item_name,cart_item.item_description))

#Step 5:  In the main section of your code, implement the print_menu() function. print_menu() has a ShoppingCart
# arameter and outputs a menu of options to manipulate the shopping cart. Each option is represented by a single
# character. Build and output the menu within the function

def print_menu(ShoppingCart): 
    
    menu_choice = ''
    
    while menu_choice != 'q':
        print('MENU')
        print('a - Add item to cart')
        print('r - Remove item from cart')
        print('c - Change item quantity')
        print('i - Output items\' descriptions')
        print('o - Output shopping cart')
        print('q - Quit')
        menu_choice = input('Choose an option: ')
        if menu_choice == 'a':
            print(menu_choice)
        elif menu_choice == 'r':
            print(menu_choice)
        elif menu_choice == 'c':
            print(menu_choice)
        elif menu_choice == 'i':
            ShoppingCart.print_descriptions() #Step 6: Implement Output shopping cart menu option. Implement Output item's description menu option
        elif menu_choice == 'o':
            ShoppingCart.print_total() # Steo 6: Implement Output shopping cart menu option

if __name__ == "__main__":

    
    #Create ShoppingCart
    ShoppingCart = ShoppingCart()

    #Prompt user for customer information
    ShoppingCart.customer_name = input('Input customer name:')
    ShoppingCart.current_date = input('Input current date:')
    
    #Create ItemsToPurchase
    Item = ItemsToPurchase()
    num_item = 1

    # Gather shopping cart entries until the user enters a 'q'
    # Initialize Sentinel Character
    user_input = ''
    while user_input != 'c':
        print('Item {}'.format(num_item))
        Item.item_name = input('Enter the item name:')
        Item.item_description = input('Enter item description:')
        Item.item_price = float(input('Enter the item price:'))
        Item.item_quantity = int(input('Enter the item quantity:'))
        ShoppingCart.add_item(Item)
        user_input = input('Enter c to continue, any other key to add another item: ')
        num_item += 1
            
    print_menu(ShoppingCart)
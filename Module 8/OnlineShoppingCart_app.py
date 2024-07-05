#Import OnlineShoppingCart_module, provides for items and shopping cart class support and user menu
import OnlineShoppingCart_module as olsc

#Online Shopping Cart Main Application

if __name__ == "__main__":
    
    #Create ShoppingCart
    shoppingCart = olsc.ShoppingCart()

    #Prompt user for customer information
    shoppingCart.customer_name = input('Input customer name:')
    shoppingCart.current_date = input('Input current date:')
    print('Customer name: {}'.format(shoppingCart.customer_name))
    print('Today\'s date: {}'.format(shoppingCart.current_date))
    
    #Create ItemsToPurchase
    item = olsc.ItemsToPurchase()
    num_item = 1

    #Call main menu
    olsc.print_menu(shoppingCart)
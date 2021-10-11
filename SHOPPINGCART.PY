# def shopping_cart():
#     while True:
#         response = input("What would you like to do? you can: quit/ add/ remove/ show or clear \n Choose only one \n")
#         if response.lower() == "quit":
#             show_cart()
#             print("Thanks for shopping")
#             break
#         elif response.lower() == 'add':
#             item = input("What would you like to add?")
#             add_item(item)
#         elif response.lower() == 'remove':
#             item = input("What would you like to remove?")
#             remove_item(item)
#         elif response.lower() == 'show':
#             show_cart()
#         elif response.lower() == 'clear':
#             clear_cart()
#         else:
#             print("Invalid Option.  Try again!")



class ShoppingCart():
	    #Creates shopping cart objects for users
    def __init__(self, items):
        self.items = items 

    def show_cart(self):
        for item in self.items:
            print(item)
		
    def add_item(self): 
        #Adds item to the cart
        item = input("What would you like to add?")
        self.items.append(item)   

        if not item in self.items:
            print(f"{item} was added to your cart.")
        else:
            print(f"{item} is already in your cart.")
	
    def remove_item(self):
		    #Remove item from the cart
        item = input("What would you like to remove?")
        if item in self.items:
            self.items.remove(item)
            print(f"{item} was removed from your cart")
        else:
            print (f"{item} is not in your cart.")

    def clear_cart():
        print("Your cart is empty")
	
        #Creating an instance of ShoppingCart
my_cart = ShoppingCart([])

def run():
    while True:
        response = input("What would you like to do? you can: quit/ add/ remove/ \n Choose only one \n")
        if response.lower() == "quit":
            my_cart.show_cart()
            print("Thanks for shopping")
            break
        elif response.lower() == 'add':
            my_cart.add_item()
        elif response.lower() == 'remove':
            my_cart.remove_item()    
        
        else:
            print("Invalid Option.  Try again!")

run()
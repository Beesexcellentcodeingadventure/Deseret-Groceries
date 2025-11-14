#Have menu system that repeats until the user chooses quit.
#Create a list that will store the names of the items in the shopping cart.
# Complete the option to add the name of the item in the shopping cart.
# Complete the option to display the names of the items in the list.

print("Welcome to Deseret Groceries!")

cart = []

shopping = True

while shopping:
    print("\nWhat would you like to do first?")
    print("1. Add Item")
    print("2. View Cart")
    print("3. Remove Item")
    print("4. Compute Total")
    print("5. Quit")

    action = int(input("Please enter an action: "))

    if action == 1:
        item = input("What item would you like to add? ")
        cart.append(item)
        print(f"'{item}' has been added to the cart.")

    elif action == 2:
        print("This is what your cart looks like right now:")
        for item in cart:
            print(item)

    elif action == 3:
        item_to_remove = input("Which item would you like to remove? ")
        if item_to_remove in cart:
            cart.remove(item_to_remove)
            print(f"'{item_to_remove}' has been removed from the cart.")
        else:
            print("That item is not in the cart.")

    elif action == 4:
        print(f"You have {len(cart)} item(s) in your cart.")

    elif action == 5:
        print("Thank you. Goodbye.")
        shopping = False

    else:
        print("Invalid action. Please try again.")
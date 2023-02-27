#Save inventory as string, makes things easier. hi
inventory = """
Here is a list of the candies we carry and their prices:
\nKit Kat : $1.00
Mnm : $1.00
Twix : $1.00
Gum : $.25
Gummies : $1.25
Mars : $1.50
Sour Worms : $1.75
"""
#Create a dictionary where the name of the candy is key and the cost is value.
candy_dict = {
            "Kit Kat" : 1.00, "Mnm's" : 1.00, 
              "Twix" : 1.00, "Gum" : .25, 
              "Gummies" : 1.25, "Mars" : 1.50, 
              "Sour Worms" : 1.75
              }
#Create an empty dict where it will take in the costumers candy of choice as key and the amount of candies as value.
#Shooping_cart = {costumers_candy : how_many_candies,} 
shooping_cart = {}

#Create function called candy store.
#Print initial welcome, and start a while loop.
def candy_store():
    print("\nHello! Welcome to 'The Candy Shop', we carry a variety of candies.\nIf you wish to continue please follow the instructions below:\n")
    while True:
    #Give user options to choose from. 
        print("If you'd like to add an item to your shopping cart, please type the command 'add'.")
        print("If you'd like to remove an item from your shopping cart please type the command 'subtract'.")
        print("If you'd like to see what's inside your shopping cart please type the command 'view'.")
        print("If you'd like to quit please type the command 'quit'.\n") 
    #Save users choice as answer using input. 
        answer = input("Please type your command: ").lower()

    #Create an if statement to add 
        if answer == 'add':
            print(inventory)
            costumers_candy = input("What would you like?\nPlease type the name of the candy that you would like to add to your shooping cart: ").title()
            how_many_candies = int(input(f"How many {costumers_candy.title()}(s) would you like? Please type a number: "))

            if costumers_candy in shooping_cart:
                shooping_cart[costumers_candy] += how_many_candies
            else:
                shooping_cart[costumers_candy] = how_many_candies
            print(f"\n{how_many_candies} {costumers_candy}(s) have been added to your shooping cart.\n")
            
        
        elif answer == 'subtract':
            print("\nItems in your shopping cart:")
            for costumers_candy, how_many_candies in shooping_cart.items():
                print(f"{how_many_candies} {costumers_candy}(s)")
            candy_subtracted = input("\nWhat item would you like to subtract? Please type the name of the candy: ").title()
            num_candies_subtracted = int(input(f"How many {candy_subtracted}(s) would you like to subtract? Please type a number: ")) 
            if candy_subtracted in shooping_cart:
                dict_of_candies_sub = {}
                dict_of_candies_sub[candy_subtracted] = num_candies_subtracted
                difference = shooping_cart[candy_subtracted] - dict_of_candies_sub[candy_subtracted] 
                shooping_cart[candy_subtracted] = difference
                print(f"{num_candies_subtracted} {candy_subtracted}(s)have been removed from your shopping cart!\n")

        elif answer == 'view': 
            print("This is what's currently in your shooping cart:\n ")
            for costumers_candy, how_many_candies in shooping_cart.items():
                print(f"{how_many_candies} {costumers_candy}(s)")

        elif answer == 'quit':
            final_total = 0
            for costumers_candy, how_many_candies in shooping_cart.items():
                price_of_candy = candy_dict[costumers_candy]
                total_cost_per_candy = price_of_candy * how_many_candies
                final_total += total_cost_per_candy
            
            print("\nReceipt:")
            for costumers_candy, how_many_candies in shooping_cart.items():
                print(f"{how_many_candies} {costumers_candy}(s): ${candy_dict.get(costumers_candy) * how_many_candies:.2f}")
            print(f"Total: ${final_total:.2f}")
            print("Thanks for shopping with us, come back anytime!")
            break

candy_store()

# Build-your-own-pizza-app
# Create a program that asks the user to choose a crust, sauce, cheese, and 3-5 total toppings to the pizza
# Features/edge cases
# a. list categories, list options within each category - eg: Crust Options: thin, pan, deep dish
# b. after category is picked, only show remaining categories and not allow category/options to be edited again
# c. allowed categories/options available, message if options not in obj
# d. casing for user input - ensure matches dict key/values

# Steps
# 1. Create categories dict with each category options in a list
# 2. Set up user input variables and print options to user
# 3. Create order dict
# 4. Iterate thru categories dict, check if choice is in options list and add choice to order dict
# 5. Iterate thru order dict and return order (after order completed)

# input: dictionary
# output: order with 1 crust, 1 cheese, 1 sauce and 3-5 topping choices - format, not sure yet

categories_1 = {
    "crust": ["thin", "pan", "deep dish"],
    "sauce": ["marinera", "olive oil"],
    "cheese": ["mozzarella", "parmesan", "mixed"],
    "toppings": ["pepperoni", "artichoke", "broccoli", "basil", "tomato"],
}


def pizza_maker(categories_dict):
    order_dict = {}

    while len(order_dict) < len(categories_dict):
        print("\nCategories:")
        for category in categories_dict:
            if category not in order_dict:
                print(category)
        # user input
        category_input = input("\nChoose your pizza category: ")
        category_choice = category_input.lower()
        # toppings condition, 3 toppings selected - needs to loop 3x
        if category_choice == "toppings":
            order_dict["toppings"] = []
            while len(order_dict["toppings"]) < 3:
                print(f"\n{category_choice.capitalize()} options: \n")
                for item in categories_dict["toppings"]:
                    if item in categories_dict["toppings"] and item not in order_dict["toppings"]:
                        print(item)
                toppings_option = input(
                    f"\nWhat type of toppings do you want? Please pick 3. ")
                if "toppings" in order_dict:
                    order_dict["toppings"].append(toppings_option)
                else:
                    order_dict["toppings"] = [toppings_option]
        elif category_choice in categories_dict and category_choice not in order_dict:
            print(f"\n{category_choice.capitalize()} options: \n")
            for option in categories_dict[category_choice]:
                print(option)
            category_option = input(
                f"\nWhat type of {category_choice} do you want? ")
            if category_option.lower() in categories_dict[category_choice]:
                order_dict[category_choice] = [category_option]
            else:
                print("Sorry this option is not on the menu.")
        else:
            print("Sorry this category is not on the menu.")

    order_summary = "\nHere's your completed order:\n"
    for category, option_lst in order_dict.items():
        toppings_str = ""
        options_str = ""
        if len(option_lst) == 1:
            order_summary += f"{category.capitalize()}: {options_str.join(option_lst)}\n"
        else:
            toppings_str = f"{category.capitalize()}: "
            for option in option_lst:
                toppings_str += option + " "
            order_summary += toppings_str
    print(order_summary)


pizza_maker(categories_1)

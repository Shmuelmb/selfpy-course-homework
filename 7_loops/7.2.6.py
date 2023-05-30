import string

print("welcome my bro, this is my crazy program")
input_from_user = (input(
    "your list (for example -> Milk, Cottage, Tomatoes): "))  # Input the list as a string (e.g., Milk, Cottage, Tomatoes)

list_market = input_from_user.split(",")  # Convert the string to a list by splitting on commas

print("the options are:\n 1-> show your list\n 2-> show length of list\n 3-> fined number in list\
       \n 4-> find his count of number the user input in the list\n 5->remove item from the list\n 6-> append item to the list\
       \n 7-> append\n 8-> remove duplicate item from list\n 9->exit")

while True:
    num = int(input("choice your num: "))

    match num:
        # Match the chosen option
        case 1:
            print(list_market)  # Show the current list

        case 2:
            print(len(list_market))  # Show the length of the list

        case 3:
            # Find an item in the list
            find_item = input("input your item that you want to find in list:")
            count_item = list_market.count(find_item)
            if count_item == 0:
                print(False)  # Item not found
            else:
                print(True)  # Item found

        case 4:
            # Find the count of an item in the list
            find_count_item = input(
                "input your item that you want find his count in the list:"
            )
            len_of_item_in_list = list_market.count(find_count_item)
            print(len_of_item_in_list)

        case 5:
            # Remove an item from the list
            remove_item = input(
                "input your item that you want remove from list:"
            )
            list_market.remove(remove_item)

        case 6:
            # Append an item to the list
            up_item = input("input you item thaht you want to add:")
            list_market.append(up_item)
            print(list_market)

        case 7:
            # Display defective items
            defective_items = []
            for items in list_market:
                if len(items) < 3:
                    defective_items.append(items)
                for item in items:
                    if item.isdigit() or item in string.punctuation:
                        defective_items.append(items)
            print(defective_items)

        case 8:
            # Remove duplicate items from the list
            list(set(list_market))

        case default:
            # Exit the program
            print("GoodBye")
            quit()

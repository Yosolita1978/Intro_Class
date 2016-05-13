shopping_list =[]

def add(item):
    global shopping_list
    if item.upper() in shopping_list or item.lower() in shopping_list:
        print "That item already exist"
        shopping_list.sort()
    else:
        shopping_list.append(item)
        return shopping_list

def remove(item):
    global shopping_list
    if item.upper() in shopping_list or item.lower() in shopping_list:
        shopping_list.remove(item)
        print "The item was removed"
        return shopping_list.sort()
    elif item not in shopping_list:
        print "That item does not exist"
    
def menu():
    menu_1 = """
    0 - Main Menu
    1 - Show current list
    2 - Add an item to your shopping list
    3 - Remove an item to your shopping list
    4 - exit """
    print "Hello, This is your menu for the Shopping List. What do you want to do:?"
    option_1 = (raw_input(menu_1))
    return option_1    

def main():
    option_1 = menu()
    while True:
        if option_1 == "1":
            print shopping_list
            option_1 = menu()
        elif option_1 == "2":
            add_item = raw_input("Please type your item or X if you're done: ")
            if add_item.upper() == "X":
                option_1 = menu()
            else:
                add(add_item)
            print shopping_list
        elif option_1 == "3":
            remove_item = raw_input("Please type your item or X if you're done: ")
            if remove_item.upper() == "X":
                option_1 = menu()
            else:
                remove(remove_item)
            print shopping_list
        elif option_1 == "4":
            break



if __name__ == '__main__':
    main()

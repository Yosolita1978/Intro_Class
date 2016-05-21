""" Whit this program that allows you to have a Shopping List we are using all the data structures that are important in python"""

general_shopping_list ={}

def add(key):
    key = key.lower()
    shopping_list = []
    if key in general_shopping_list:
        print "That list %s already exist" %(key)     
    else:
        general_shopping_list[key] = shopping_list
        print "Your list %s was created" %(key)

def remove(key):
    key = key.lower()
    if key in general_shopping_list:
        del general_shopping_list[key]
        print "Your list %s has been removed" %(key)     
    else:
        print "That list does not exist"

def show_list():
    print general_shopping_list

def show_a_list(key):
    global general_shopping_list
    key = key.lower()
    if key in general_shopping_list:
        shopping_list = general_shopping_list[key]
        shopping_list.sort()
        print shopping_list
    else:
        print "That list doesn't exist"

def add_item(key, item):
    key = key.lower()
    item = item.lower()
    if key in general_shopping_list:
        #shopping_list = general_shopping_list[key]
        if item not in general_shopping_list[key]:
            general_shopping_list[key].append(item)
            print "This is your new Shopping List %s " %(general_shopping_list[key])
        else:
            print "This item %s already exist!" %(item)
    else:
        print "Sorry, There is no list with that name"

def remove_item(key, item):
    key = key.lower()
    item = item.lower()
    if key in general_shopping_list:
        shopping_list = general_shopping_list[key]
        if item in shopping_list:
            shopping_list.remove(item)
            print "This item %s has been removed. Here is your list: %s" %(item, shopping_list)
        else:
            print "There is not %s item in your list" %(item)
    else:
        print "Sorry, There is no list with that name"    

def separated_comma(string):
    split_string = string.replace(" ","").split(",")
    return split_string 


    
def menu():
    menu_1 = """
    0 - Main Menu
    1 - Show all list
    2 - Show a specific list
    3 - Add a new Shopping list
    4 - Add an item to a shopping list
    5 - Remove an item from a shopping list
    6 - Remove a list by nickname
    7 - Exit """
    print "Hello, This is your menu for the Shopping List. What do you want to do:?"
    option_1 = (raw_input(menu_1))
    return option_1    

def main():
    option_1 = menu()
    while True:
        if option_1 == "0":
            option_1 = menu()
        elif option_1 == "1":
            show_list()
            option_1 = menu()
        elif option_1 == "2":
            showme_list = raw_input("Please type what list do you want to see or X to exit: ")
            if showme_list.upper() == "X":
                option_1 = menu()
            else:
                show_a_list(showme_list)
                option_1 = menu()
        elif option_1 == "3":
            addmy_list = raw_input("Please type the name of the list you want to create or X to exit: ")
            if addmy_list.upper() == "X":
                option_1 = menu()
            else:
                add(addmy_list)
                option_1 = menu()
        elif option_1 == "4":
            my_list = raw_input("Please type the name of the list that you want to modificate: ")
            my_items = raw_input("Please type the items (separated by comma) that you want to add or X to exit: ")
            if my_items.upper() == "X":
                option_1 = menu()
            else:
                for my_item in separated_comma(my_items): 
                    add_item(my_list, my_item)
                option_1 = menu()
        elif option_1 == "5":
            my_list = raw_input("Please type the name of the list that you want to modificate: ")
            my_items = raw_input("Please type the items (separated by comma) that you want to remove or X to exit: ")
            if my_items.upper() == "X":
                option_1 = menu()
            else:
                for my_item in separated_comma(my_items): 
                    add_item(my_list, my_item)
                option_1 = menu()
        elif option_1 == "6":
            removemy_list = raw_input("Please type the name of the list that you want to remove or X to exit: ")        
            if removemy_list.upper() == "X":
                option_1 = menu()
            else:
                remove(removemy_list)
                option_1 = menu()
        elif option_1 == "7":
            break



if __name__ == '__main__':
    main()

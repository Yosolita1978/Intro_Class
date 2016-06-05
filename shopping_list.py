""" Whit this program that allows you to have a Shopping List we are using all the data structures that are important in python"""
import json 
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
    global general_shopping_list
    for key in general_shopping_list:
        print "Your list %s has this items: " %(key)
        for value in general_shopping_list[key]:
            print "* %s" %(value)


def show_a_list(key):
    global general_shopping_list
    key = key.lower()
    if key in general_shopping_list:
        shopping_list = general_shopping_list[key]
        shopping_list.sort()
        print "Your list %s has this items: %s " %(key,shopping_list)
    else:
        print "That list doesn't exist"

def add_item(key, item):
    key = key.lower()
    item = item.lower()
    if key in general_shopping_list:
        #shopping_list = general_shopping_list[key]
        if item not in general_shopping_list[key]:
            general_shopping_list[key].append(item)
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
        else:
            print "There is not %s item in your list" %(item)
    else:
        print "Sorry, There is no list with that name"    

def separated_comma(string):
    split_string = string.replace(" ","").split(",")
    return split_string 

def write_list():
    with open('/Users/cristina/Source/intro_class_cristina/shopping_list.txt',"w") as my_file:
        my_file.write(json.dumps(general_shopping_list))
        # for key,value in general_shopping_list.iteritems():
        #     my_file.write(key)
        #     my_file.write("=")
        #     my_file.write(",".join(value))
        #     my_file.write("\n")

def read_list():
    global general_shopping_list
    with open('/Users/cristina/Source/intro_class_cristina/shopping_list.txt') as my_file:
        general_shopping_list = json.loads(my_file.read())
        # for line in my_file:
        #     key,value = line.split("=")
        #     value = value.replace("\n", "").split(",")
        #     general_shopping_list[key]= value

    
def menu():
    menu_1 = """
    0 - Main Menu
    1 - Show all list
    2 - Show a specific list
    3 - Add a new Shopping list
    4 - Add items to a shopping list
    5 - Remove items from a shopping list
    6 - Remove a list by nickname
    7 - Print your list in a file
    8 - Exit """
    print "Hello, This is your menu for the Shopping List. What do you want to do:?"
    option_1 = (raw_input(menu_1))
    return option_1    

def main():
    try:
        read_list()
    except IOError:
        pass    
    option_1 = menu()
    while True:
        if option_1 == "1":
            show_list()

        elif option_1 == "2":
            showme_list = raw_input("Please type what list do you want to see or X to exit: ")
            if showme_list.upper() != "X":
                show_a_list(showme_list)    
            
        elif option_1 == "3":
            addmy_list = raw_input("Please type the name of the list you want to create or X to exit: ")
            if addmy_list.upper() != "X":
               add(addmy_list)

        elif option_1 == "4":
            my_list = raw_input("Please type the name of the list that you want to modify: ")
            my_items = raw_input("Please type the items (separated by comma) that you want to add or X to exit: ")
            if my_items.upper() != "X":
                for my_item in separated_comma(my_items): 
                    add_item(my_list, my_item)
                show_a_list(my_list)

        elif option_1 == "5":
            my_list = raw_input("Please type the name of the list that you want to modify: ")
            my_items = raw_input("Please type the items (separated by comma) that you want to remove or X to exit: ")
            if my_items.upper() != "X":
                for my_item in separated_comma(my_items): 
                    add_item(my_list, my_item)
                show_a_list(my_list)

        elif option_1 == "6":
            removemy_list = raw_input("Please type the name of the list that you want to remove or X to exit: ")        
            if removemy_list.upper() != "X":
                remove(removemy_list)

        elif option_1 == "7":
            write_list() 

        elif option_1 == "8":
            break

        option_1 = menu()



if __name__ == '__main__':
    main()

""" This program will help you decide is you should eat bacon. Hint: you should """

def eat_bacon():
    print "Eat it, eat some bacon"

def eat_maybe():
    question = raw_input("Are you a coward? Yes or No ")
    if question == "Yes":
        print "You're a coward but Bacon will turn you into a true warrior"
        eat_bacon()
    elif question == "No":
        print "You're not a coward"
        eat_bacon()



def main():
    prompt1 = "Do you want to feel like angels are frolicking on your taste buds "\
    + "\n" + "1 - yes" + "\n" + "2 - no" + "\n" + "3 - yes but I'm afraid bacon will kill me "
    choice = int(raw_input(prompt1))

    if choice == 1:
        eat_bacon() 
    elif choice ==2:
        print "You've clearly never tasted bacon"
        eat_bacon()
    elif choice == 3:
        eat_maybe()

if __name__ == '__main__':
    main()
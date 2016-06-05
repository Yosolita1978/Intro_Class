from send_sms import send_SMS 
contact_list = []

class Contact(object):

    def __init__(self, first_name, last_name, mobile="", email="", home_number="",address="", twitter=""):
        self.first_name = first_name
        self.last_name = last_name
        self.mobile = mobile
        self.email = email
        self.home_number = home_number
        self.address = address
        self.twitter = twitter


    def edit_contact(self):
        edit_question = raw_input("""
            What do you want to edit:
            1. First Name
            2. Last Name
            3. Mobile
            4. Email
            5. Home Number
            6. Address
            7. Twitter """)
        if edit_question == "1":
            edit_firstname = raw_input("What is the new First Name: ")
            self.first_name = edit_firstname
        elif edit_question == "2":
            edit_lastname = raw_input("What is the new Last Name: ")
            self.last_name = edit_lastname
        elif edit_question == "3":
            edit_mobile = raw_input("What is the new mobile phone: ")
            self.mobile = edit_mobile
        elif edit_question == "4":
            edit_email = raw_input("What is the new email: ")
            self.email = edit_email
        elif edit_question == "5":
            edit_homenumber = raw_input("What is the new home number: ")
            self.home_number = edit_homenumber
        elif edit_question == "6":
            edit_address = raw_input("What is the new address: ")
            self.address = edit_address
        elif edit_question == "7":
            edit_twitter = raw_input("What is the new twitter: ")
            self.twitter = edit_twitter
        else:
            print "Sorry, That is not a valid option"
            self.edit_contact()


    def send_message(self):
        if self.mobile.isdigit() == True:
            mobile_sms = "+" + self.mobile
            message = raw_input("What message do you want to send: ")
            send_SMS(mobile_sms, message)
        else:
            print "I'm sorry, that contact doesn't have a mobile number"

    def send_twitter(self):
        print "This will send you a twitter to %s" %(self.twitter)

    def __str__(self):
        return  """
                First Name:  %s
                Last Name:   %s
                Mobile:      %s
                Home Number: %s
                Email:       %s
                Address:     %s
                Twitter:     %s
                """ %(self.first_name, self.last_name, self.mobile, self.home_number, self.email, self.address, self.twitter ) 
    
    def show_contact(self):
        print self


def find_contact(first_name, last_name):
    for contact in contact_list:
        if contact.first_name == first_name and contact.last_name == last_name:
            return contact
    return None


def add_contact(first_name, last_name, mobile="", email="", home_number="", address="", twitter=""):
    contact = find_contact(first_name, last_name)
    if contact is None:
        new_contact = Contact(first_name, last_name, mobile, email, home_number, address, twitter)
        contact_list.append(new_contact)
        new_contact.show_contact()
        show_contactlist(contact_list)
    else:
        print "The contact %s, %s already exist" %(first_name, last_name)
     

def remove_contact(first_name, last_name):
    contact = find_contact(first_name, last_name)
    if contact is None:
        print "The contact %s %s does not exist in your Contact List" %(first_name, last_name)
    else:
        ask_user = raw_input("Are you sure you want to remove the contact %s %s. Yes or No? " %(first_name, last_name))
        if ask_user.lower() == "Yes":
            contact_list.remove(contact)
            show_contactlist(contact_list)
        return 

def search_contact(first_name, last_name):
    contact = find_contact(first_name, last_name)
    if contact is None:
        print "The contact %s %s is not in your Contact List" %(first_name, last_name)
    else:
        contact.show_contact()

def edit_contact(first_name, last_name):
    contact = find_contact(first_name,last_name)
    if contact is None:
        print "The contact %s %s is not in your Contact List" %(first_name, last_name)
    else:
        contact.edit_contact()
        contact.show_contact()

def send_sms(first_name, last_name):
    contact = find_contact(first_name, last_name)
    if contact is None:
        print "The contact %s %s is not in your Contact List" %(first_name, last_name)
    else:
        contact.send_message()

def send_tweet(first_name, last_name):
    contact = find_contact(first_name, last_name)
    if contact is None:
        print "The contact %s %s is not in your Contact List" %(first_name, last_name)
    else:
        contact.send_twitter()

def show_contactlist(list):
    if contact_list != []:
        for contact in contact_list:
            print contact.first_name, contact.last_name
    else:
        print "Your Contact List is empty"

def parse_field(string):
    string = string.split(":")[1].strip()
    return string

def write_list():
    with open('/Users/cristina/Source/intro_class_cristina/contact_list.txt',"w") as my_file:
        for contact in contact_list:
            my_file.write(str(contact))

def read_list():
    global contact_list
    with open('/Users/cristina/Source/intro_class_cristina/contact_list.txt') as my_file:
        contact = None
        for line in my_file:
            line = line.strip()
            if line == "":
                pass
            elif line.startswith("First Name"):
                contact_firstname = parse_field(line)
            elif line.startswith("Last Name"):
                contact_lastname = parse_field(line)
                contact = Contact(contact_firstname, contact_lastname)
            elif line.startswith("Mobile"):
                contact.mobile = parse_field(line)
            elif line.startswith("Home Number"):
                contact.home_number = parse_field(line)
            elif line.startswith("Email"):
                contact.email = parse_field(line)
            elif line.startswith("Address"):
                contact.address = parse_field(line)
            elif line.startswith("Twitter"):
                contact.twitter = parse_field(line)
                contact_list.append(contact)
    show_contactlist(contact_list)


def menu_contact():
    user_choice = raw_input("""
    This is your Contact Manager. What do you want to do:
    1. Read your Contact List 
    2. Add a Contact
    3. Edit a Contact
    4. Remove a Contact
    5. Search for a Contact
    6. Send a SMS to a Contact
    7. Send a Tweet to a Contact
    8. Write your Contact List in a .txt
    9. Show your Contact List
    10. Exit """)
    return user_choice


def main():
    
    user_choice = menu_contact()
    
    while True:
        if user_choice == "1":
            read_list()

        elif user_choice == "2":
            first_name = raw_input("Please type the First Name of your new contact: ")
            last_name = raw_input("Please type the Last Name of your new contact: ")
            contact = add_contact(first_name, last_name)            


        elif user_choice == "3":
            user_edit_first_name = raw_input("Please type the First Name of the contact to edit: ")
            user_edit_last_name = raw_input("Please type the Last Name of the contact to edit: ")
            edit_contact(user_edit_first_name, user_edit_last_name)

        elif user_choice == "4":
            user_remove_first_name = raw_input("Please type the First Name of the contact to remove: ")
            user_remove_last_name = raw_input("Please type the Last Name of the contact to remove: ")
            remove_contact(user_remove_first_name, user_remove_last_name)

        elif user_choice == "5":
            user_search_first_name = raw_input("Please type the First Name of the contact to search: ")
            user_search_last_name = raw_input("Please type the Last Name of the contact to search: ")
            search_contact(user_search_first_name, user_search_last_name)

        elif user_choice == "6":
            user_sms_first_name = raw_input("Please type the First name of the contact to send a SMS: ")
            user_sms_last_name = raw_input("Please type the Last name of the contact to send a SMS: ")
            send_sms(user_sms_first_name, user_sms_last_name)

        elif user_choice == "7":
            user_tweet_first_name = raw_input("Please type the First name of the contact to send a Tweet: ")
            user_sms_tweet_name = raw_input("Please type the Last name of the contact to send a Tweet: ")
            send_tweet(user_tweet_first_name, user_teet_last_name)

        elif user_choice == "8":
            write_list()

        elif user_choice == "9":
            show_contactlist(contact_list)

        else:
            break

        user_choice = menu_contact()
    
    


    

if __name__ == '__main__':
    main()

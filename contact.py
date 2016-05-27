class Contact(object):

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.mobile = ""
        self.email = ""
        self.home_numer = ""
        self.adress = ""
        self.twitter = ""


    def send_message(self, mobile):
        if mobile.isdigit() == True:
            return "This will send you a SMS to the No: %s" % (self.mobile)
        else:
            return False

    def send_twitter(self,twitter):
        return "This will send you a twitter to %s" %(self.twitter)


def main():
    contacts_list = []
    contact1 = Contact("Cristina","Rodriguez")
    contact2 = Contact("Jair", "Trejo")
    contact3 = Contact("Rocio","Garcia")

    contacts_list.append(contact1)
    contacts_list.append(contact2)
    contacts_list.append(contact3)

    contact1.mobile = "5540825723"
    contact2.mobile = "4154260010"
    contact3.mobile = "3103110866"

    contact1.twitter = "@yosola"
    contact2.twitter = "@jairtrejo"


    for item_contact in contacts_list:
        print item_contact.first_name, item_contact.last_name

    print contact1.send_message(contact1.mobile)

    print contact2.send_twitter(contact2.twitter)

if __name__ == '__main__':
    main()

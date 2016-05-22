def email_validation(email):
    part = "name"
    first_part = []
    second_part = []
    third_part = ["com", "org", "net", "edu", "mal", "gov", "com.mx", "com.co"]
    for letter in email:
        if part == "name":    
            if len(first_part) == 0 and letter == "@":
                print "That is not a valid email 1"
                return False
            elif len(first_part) != 0 and letter == "@":
                part = "domain"
            else:
                first_part.append(letter)
        elif part == "domain":
            if letter == "@":            
                print "That is not a valid email 2"
                return False
            elif len(second_part) != 0 and letter == ".":
                part = "com"    
            else:
                second_part.append(letter)
        elif part == "com":
            if len(third_part) == 0 and letter == ".":
                print "That is not a valid email 3"
                return False
        else:
            if part not in third_part:
                print "That is not a valid email 4"
                return False
            else:
                return True
                "Thank you, your email is valid" 

    if part != "com":
        print "That is not a valid email 5"
    else:
        print "Thank you, your email is valid"        

prompt = "Please, enter your email: "
email = raw_input(prompt)
email_validation(email)





        

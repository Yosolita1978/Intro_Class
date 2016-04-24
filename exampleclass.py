input = raw_input("Did you finish Activity 1?")
done = input


if (str.lower(input) == "yes"): #why do this?
    done = True
else: 
    done = False

if not done:
    print "Please continue with Activity 1."
else: 
    print "Please move on to Activity 2."
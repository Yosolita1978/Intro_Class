print "Welcome to the survey!"
name1 = raw_input("What is your name?: ")
name2 = raw_input("and what is your name?: ")
color1 = raw_input("What is your favorite color %s?: " %(name1))
color2 = raw_input("and what is your favorite color %s?: " %(name2))
hobby1 = raw_input("What is your favorite hobby %s?: " %(name1))
hobby2 = raw_input("and what is your favorite hobby %s?: " %(name2))
movie1 = raw_input("What is the last movie that you saw %s?: " %(name1))
movie2 = raw_input("and what is the last movie that you saw %s?: " %(name2))
music1 = raw_input("What is your favorite type of music %s?: " %(name1))
music2 = raw_input(" and what is your favorite type of music %s?: " %(name2))
adress1 = raw_input("Where do you live %s?: " %(name1))
adress2 = raw_input("and where do you live %s?: " %(name2))
print "%s's favorite color is %s, and %s's favorite color is %s." %(name1, color1, name2, color2)
print "%s's favorite hobby is %s, and %s's favorite hobby is %s." %(name1, hobby1, name2, hobby2)
print "%s's last movie was %s and %s's last movie  was %s." %(name1, movie1, name2, movie2) 
print "%s's favorite type of music is %s and %s's favorite type of music is %s." %(name1, music1, name2, music2)
print "%s is living in %s and %s is living in %s" %(name1, adress1, name2, adress2)

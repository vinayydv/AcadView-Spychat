print "Welcome to Spy Chat"

#This loop is to re ask the user its name just in case he/she doesnot enter the name at first time
for e in range (1,3):
    #details about the spy
    spy_name = raw_input("What do you want to be called as a spy?\n")
    if len(spy_name) > 0:

                print "Hello " + spy_name

                spy_salutation = raw_input("\nHow do you want to be saluted as Mr , Miss or plz mention anyhting else !\n")
                # concatinating name and salutation
                spy_name = spy_salutation +" "+ spy_name

                spy_age = raw_input("\nWhat is your age ?\n")
                spy_age = int(spy_age)

                #Authenticating the spy age
                if spy_age > 12 and spy_age < 30:
                    print  "\nOk! " +spy_name+ " aged " + str(spy_age)+ ". Good to have you here :) ."
                    print "\nHow about you tell something more about yourself"

                    #this loop is to reconfirm the spy ratings ..in case user enters wrong credentials
                    for e in range(1,3):

                        spy_rating = raw_input("\nWhat is your spy rating\n")
                        spy_rating = float(spy_rating)

                        # Authenticating the spy rating
                        if spy_rating >= 4.5 and spy_rating <= 5:
                                print "\nJhakaas!! ! Congratulations! You are good enough to be a spy\n"
                                break
                        elif spy_rating >= 3.5 and spy_rating < 4.5:
                                print "\nMast! ! Congratulations! You are good enough to be a spy\n"
                                break
                        elif spy_rating >= 2.5 and spy_rating < 3.5:
                                print "\nMahnat krni padegi but still ! Congratulations! You are good enough to be a spy"
                                break
                        elif spy_rating >= 0 and spy_rating < 2.5:
                                print "\nSorry ! You are not smart enough to continue here."
                                break
                        else:
                                print "\nPlease enter valid rating in the range of 0 to 5\n"

                else:
                     print "\nSorry ! " + spy_name + ". You are not good enough to be a spy\n"

                break
    else:
            print "You must enter your name to continue.!"

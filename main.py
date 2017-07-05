print "Welcome to Spy Chat"

#details about the spy
spy_name = raw_input("What do you want to be called as a spy?")
if len(spy_name) > 0:

            print "Hello " + spy_name

            spy_salutation = raw_input("How do you want to be saluted as Mr , Miss or plz mention anyhting else !")
            # concatinating name and salutation
            spy_name = spy_salutation + spy_name

            spy_age = raw_input("What is your age ?")
            spy_age = int(spy_age)

            #Authenticating the spy age
            if spy_age > 12 and spy_age < 30:
                print  "Ok! " +spy_name+ " aged " + str(spy_age)+ ". Good to have you here :) ."
                print "How about you tell something more about yourself"

                spy_rating = raw_input("What is your spy rating")
                spy_rating = float(spy_rating)

                # Authenticating the spy rating
                if spy_rating >= 4.5 and spy_rating <= 5:
                        print "Jhakaas!! ! Congratulations! You are good enough to be a spy"
                elif spy_rating >= 3.5 and spy_rating < 4.5:
                        print "Mast! ! Congratulations! You are good enough to be a spy"
                elif spy_rating >= 2.5 and spy_rating < 3.5:
                        print "Mahnat krni padegi but still ! Congratulations! You are good enough to be a spy"
                elif spy_rating >= 0 and spy_rating < 2.5:
                        print "Sorry ! You are not smart enough to continue here."
                else:
                        print "Please enter valid rating in the range of 0 to 5"

            else:
                 print "Sorry ! " + spy_name + ". You are not good enough to be a spy"


else:
        print "You must enter your name to continue.!"

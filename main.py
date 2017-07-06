import sys
from time import sleep
from spy_details import spy_name,spy_age,spy_salutation,spy_is_online,spy_rating

STATUS_MESSAGES = ['Status Message 1', 'Status Message 2', 'Status Message 3']

welcome = "W E L C O M E  T O  S P Y C H A T\n\n"
for l in welcome:
 sys.stdout.write(l)
 sys.stdout.flush()
 sleep(0)

#Fuction to update or add new status
def add_status():

    current_status_message = None

    updated_status_message = None


    if current_status_message != None:
        print "Your current status message is %s \n" % (current_status_message)
    else:
        print  "You do not have any current status\n"

    for e in range(1,3):
        default = raw_input("Do you want to select from the older status (y/n)? ")

        if default.upper() == "N":
            new_status_message = raw_input("Please Enter your new status")

            for e in range(1,3):

                if len(new_status_message) > 0:
                    STATUS_MESSAGES.append(new_status_message)#Appends the new message to the messages list
                    updated_status_message = new_status_message
                    break

                else:
                    print "You can not leave this blank. Please Enter your status."
            break
        elif default.upper() == "Y":
            if len(STATUS_MESSAGES) > 0:

                item_position = 1

                for e in STATUS_MESSAGES:

                    print '%d. %s' % (item_position, e)
                    item_position = item_position + 1

                message_selection = int(raw_input("\nChoose from the above messages "))

                if len(STATUS_MESSAGES) >= message_selection:

                    updated_status_message = STATUS_MESSAGES[message_selection - 1]

                break
            else:
                print "Sorry ! You do not have any older messages"
                break
        else:
            print "You must choose a value from Y or N"


    if updated_status_message:
        print '\nYour updated status message is: %s\n' % (updated_status_message)
    else:
        print '\nYou did not update your status message\n'


    return updated_status_message


#This function takes values from spy_details.py. It will be used to intialize processes.
def start_chat(spy_name, spy_age, spy_rating):
    print "\nWelcome %s %s ! Good to see you again :)\n"%(spy_salutation,spy_name)
    #Just to make the output look more interative this function is used to delay the print statements
    sys.stdout.flush()
    sleep(.3)

    #To ask the spy what to do.
    print "What do you want to do? Please select in following option. \n "
    sys.stdout.flush()
    sleep(.2)
    #this for loop is to re enter the option just in case wrong credential is entered by the user
    for e in range (1,3):
        menu_choice = raw_input(" 1. Add a status update \n 2. Add a friend \n 3. Send a secret message \n 4. Read a secret message \n 5. Read Chats from a user \n 6. Close Application \n")
        if len(menu_choice) > 0:
            menu_choice = int(menu_choice)

            if menu_choice == 1:
                print 'You chose to update the status\n\n'
                add_status()

                break
            else:
                print "Please select a valid option"


#This loop is to re ask the user ..in case he/she enters the wrong credentials
for e in range (1,3):
    question = raw_input( "Do you want to continue as %s %s (Y/N)\n"%(spy_salutation, spy_name))
    question = question.upper()

    if question == "Y":
        start_chat(spy_name,spy_age,spy_rating)
        break

    elif question == "N":
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
        break
    else:
        print "\nOnly select from Y and N\n"
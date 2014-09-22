#!/usr/env/python

donor_list = [
    ("John Doner", [1500]),
    ("Mary Doner", [900, 1800, 2000]),
    ("Joe Smith", [100, 150, 175]),
    ("Bob Andrews", [250, 250]),
    ("Cindy Brown", [800])
]



def main_menu():
    menu_select = raw_input("Please select: (1) Send a thank you note; (2) Create a report > ")
    
    #SEND THANK YOU
    if menu_select == "1":
        
        user_inp = raw_input("Please enter donor's full name. > ")
        while user_inp == "list":
            print donor_list
            user_inp = raw_input("Please enter donor's full name. > ")
        if user_inp not in donor_list:
            donation = int(raw_input("Donation amount? > "))
            #while not donation.isdigit():
                #donation = raw_input("Donation amount? > ")
            donor_list.append((user_inp,[donation]))

        if user_inp == "HOME":
            main_menu()

    #CREATE REPORT
    elif menu_select == "2":
        pass



def thank_you(name):
    return """Dear %s,

    Thank you so much for your generous donation of $%i! Every dollar
    helps local families in need, and none of it would be possible without
    the generosity of loyal donors like you.

    Sincerely,
    Bob Smith""" % (donor, amount)



def report():
    pass



if __name__ == '__main__':
    
    main_menu()

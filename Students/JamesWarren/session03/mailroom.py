#!/usr/bin/env python
import io

donor_list = {
    "John Doner": [1500],
    "Mary Doner": [900, 1800, 2000],
    "Joe Smith": [100, 150, 175],
    "Bob Andrews": [250, 250],
    "Cindy Brown": [800]
}

def safe_input(question):
    while True:
        try:
            return raw_input(question)
            break
        except EOFError:
            return None
        except KeyboardInterrupt:
            return None

def main_menu():
    print "---------- HOME ----------"
    print
    print "Type EXIT to quit."
    menu_select = safe_input("Please select: (1) Send a thank you note; \
(2) Create a report > ")
    
    #SEND THANK YOU
    if menu_select == "1":
        print
        print "---------- THANK YOU ----------"
        print
        print "To return to the main menu, type 'HOME'."
        user_inp = safe_input("Please enter donor's full name, or type \
'list' to see complete list of donors. > ")
        if user_inp == "HOME":
            main_menu()
        if user_inp == "list":
            print
            for (key, value) in donor_list.items():
                print (key, value)
            user_inp = safe_input("Please enter donor's full name. > ")
        while True:
            donation = safe_input("Donation amount? > ")
            try:
                donation = int(donation)
                break
            except ValueError:
                print "Please enter a valid number."
                continue
        donor_list.setdefault(user_inp, []).append(donation)
        print
        print thank_you(user_inp, donation)
        main_menu()


    #CREATE REPORT
    elif menu_select == "2":
        report()

def thank_you(name,amount):
    f = io.open('thank_you_%s.txt' % name, mode='w')
    f.write(u"""Dear %s,

Thank you so much for your generous donation of $%i! Every dollar 
helps local families in need, and none of it would be possible without 
the generosity of loyal donors like you. 

Sincerely, 
Bob Smith""" % (name, amount))
    f.close()
    print "Your thank you note has been saved to thank_you_%s.txt" % name

def report():
    print
    print "---------- REPORT ----------"
    print
    print "Name".ljust(24) + "Total Donated".ljust(16) + \
    "No. Donations".ljust(16) + "Avg. Donation".ljust(16)
    for key, value in donor_list.iteritems():
        tot_donations = sum(value)
        num_donations = len(value)
        avg_donations = tot_donations / num_donations
        print key.ljust(24) + "$"+str(tot_donations).ljust(15) + \
        str(num_donations).ljust(16) + "$"+str(avg_donations).ljust(15)
    print
    print "End of report"
    main_menu()

if __name__ == '__main__':  
    main_menu()
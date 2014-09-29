#!/usr/bin/env python2.7

import time

# Using session04 approaches
defaultdonors = {
'Harry' : [1000, 5000, 10000],
'Franklin' : [1000, 500, 750],
'George' : [950, 760],
'Dwight' : [1100, 3500],
'Dean' : [8000]
}

#Mailroom Function
def main_menu(donors=defaultdonors):
    action = 0
    while action not in ['1', '2', '3', 'q']:
        print '''
        Mailroom Menu:
        1. Send a Thank You
        2. Create a Report
        3. Special Thank You to All Donors
        Type "MM" at any prompt to return to this menu.
        Type "q" to exit script.
        '''
        action = raw_input('Enter the number from the menu above: ')
        dmenu = {'1' : thank_you, '2' : report, '3' : thankall}  #Couldn't include break to dictionary for key 'q'
        if action in dmenu.keys():
            dmenu[action](donors)
        elif action == 'q':
            break
        action = 0
    return

#Thank you menu
def thank_you(donors):
    while True:

        thank = raw_input('Enter "list" for donors, donor name, or name to be added: ')

        # Go back to Mailroom Menu
        if thank == 'MM':
            return donors

        # List of donors enetered.
        elif thank == 'list':
            print donors.keys()
            continue

        # Enter donation for current donor.
        elif thank in donors.keys():
            while True:
                donation = raw_input("Please enter a valid donation amount for current donor ($): ")
                if donation == 'MM':
                    return donors
                try:
                    if int(donation): #Evaluates if donation is an integer. Goes to except if not.
                        break
                except ValueError: #Overrides error
                    continue
                    # .isdigit()
            donors[thank].append(int(donation))
            foo = thank + '_' + time.strftime("%y_%m_%d_%H_%M_%S") + '.txt'
            bar = '''
Thank you %s for you generous donation of $%i. Your ongoing support
is appreciated due to the costs incurred for procuring otoro. If you
continue to donate, we will consider taking you to experience otoro
among other like minded otoro-lovers. Again, thank you and we hope
you have already found a way to incorporate otor in your daily life.
            ''' % (thank, int(donation))
            print bar
            donfiles = open(foo, 'w')
            donfiles.write(bar)
            donfiles.close()
            continue

        #Entering a new donor (includes verification and donation).
        else:
            verify = 'a'
            while verify not in ['n', 'y']:
                if verify in ['n', 'y']:
                    break
                elif verify == 'MM':
                    return donors
                verify = raw_input('Add %s to the donor list (y, n)? ' % thank)
            if verify == 'y':
                donors[thank] = []  #Use append instead of add.
                #donors.append([])#donors + ([thank, []])#.append([thank, []])
                while True:
                    donation = raw_input("Please enter a valid donation amount for new donor ($): ")
                    if donation == 'MM':
                        return donors
                    try:  #Evaluates if donation is an integer. Goes to except if not.
                        if int(donation):  # Try .isdigit()
                            break
                    except ValueError:  #Overrides ValueError and continues in loop.
                        continue
                #donorhistoryloc = 1 + donors.index(thank)  #Find corresponding donation to name
                donors[thank].append(int(donation))#[:][donorhistoryloc].append(int(donation))  #Add value in 'donation' to donor's list
                foo = thank + '_' + time.strftime("%y_%m_%d_%H_%M_%S") + '.txt'
                bar = '''
Thank you %s for your first time generous donation of $%i. These
funds will provide George Nuesca with further chances to eat
sushi, especially otoro. Your donation will also help establish a
fund to bring additional guests to future otoro adventures. If you
would like to donate otoro directly, please contact our stockhouse.
We hope one day you too can enjoy otoro, possibly with us!
                ''' % (thank, int(donation))
                print bar
                donfiles = open(foo, 'w')
                donfiles.write(bar)
                donfiles.close()
            elif verify == 'n':
                None
            continue

#Create a report of donors
def report(donors):
    # Table formatting.
    print '{0:<20}     {1:^13}     {2:^19}     {3:^20}'.format('Name','Total Donated',
        'Number of Donations', 'Average per Donation')
    print '-' * 91
    # Calculate report.
    for k in sorted(donors, key = lambda k: len(donors[k]), reverse = True):
        print '{0:<20}     {1:^13}     {2:^19}     {3:^20}'.format (k,
            sum(donors[k]), len(donors[k]), sum(donors[k])/len(donors[k]))
    return donors

def thankall(donors):
    dthank = {'a' : 'Dear ',
    'b' : 'We were just thinking of you and what you have donated to the eat\n',
    'c' : 'otoro cause. We want to take a moment to let you know we not only\n',
    'd' : 'use your donation to procure otoro for dining experiences, but\n',
    'e' : 'to also contribute to sustainable bluefin aquaculture facilities.\n',
    'f' : 'We believe this will help prevent wild bluefin extinction and\n',
    'g' : 'promote otoro spawning, all while we can enjoy the delicacy from\n',
    'h' : 'a gastronomy aspect. Again, we appreciate all you have done.\n',
    'i' : '-Otoro Eating Team\n'
    }
    for donor in donors.keys():
        foo = '{a}{0}\n{b}{c}{d}{e}{f}{g}{h}{i}'.format(donor, **dthank)
        bar = donor + '_specialthanks_' + time.strftime("%y_%m_%d_%H_%M_%S") + '.txt'
        donfiles = open(bar, 'w')
        donfiles.write(foo)
        donfiles.close()

if __name__ == '__main__':
    main_menu()
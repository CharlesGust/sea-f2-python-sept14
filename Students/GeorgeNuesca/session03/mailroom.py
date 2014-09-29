#!/usr/bin/env python2.7

# Using session04 approaches
defaultdonors = [
'Harry', [1000, 5000, 10000],
'Franklin', [1000, 500, 750],
'George', [950, 760],
'Dwight', [1100, 3500],
'Dean', [8000]
]

#Mailroom Function
def main_menu(donors=defaultdonors):
    action = 0
    while action not in ['1', '2', 'q']:#(action != '1') or (action != '2') or (action != 'q'):  # Exits with the following sytax--> action not in ['1', '2', 'q']:
        print '''
        Mailroom Menu:
        1. Send a Thank You
        2. Create a Report
        Type "MM" at any prompt to return to this menu.
        Type "q" to exit script.
        '''
        action = raw_input('Enter the number from the menu above: ')
        if action == '1':
            thank_you(donors)
        elif action == '2':
            report(donors)
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
            print donors[::2]
            continue

        # Enter donation for current donor.
        elif thank in donors[::2]:
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
            donorhistoryloc = 1 + donors.index(thank) #Find corresponding donation to name
            donors[:][donorhistoryloc].append(int(donation)) #Add value in 'donation' to donor list
            print '''
            Thank you %s for you generous donation of $%i. Your ongoing support
            is appreciated due to the costs incurred for procuring otoro. If you
            continue to donate, we will consider taking you in a group to
            experience otoro for yourself. Again, thank you and we hope you
            have already found a way to incorporate otor in your daily life.
            ''' % (thank, int(donation))
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
                donors.append(thank)  #Use append instead of add.
                donors.append([])#donors + ([thank, []])#.append([thank, []])
                while True:
                    donation = raw_input("Please enter a valid donation amount for new donor ($): ")
                    if donation == 'MM':
                        return donors
                    try:  #Evaluates if donation is an integer. Goes to except if not.
                        if int(donation):  # Try .isdigit()
                            break
                    except ValueError:  #Overrides ValueError and continues in loop.
                        continue
                donorhistoryloc = 1 + donors.index(thank)  #Find corresponding donation to name
                donors[:][donorhistoryloc].append(int(donation))  #Add value in 'donation' to donor's list
                print '''
                Thank you %s for your first time generous donation of $%i. These
                funds will provide George Nuesca with further chances to eat
                sushi, especially otoro. Your donation will also help establish a
                fund to bring additional guests to future otoro adventures. If you
                would like to donate otoro directly, please contact our stockhouse.
                We hope one day you too can enjoy otoro, possibly with us!
                ''' % (thank, int(donation))
            elif verify == 'n':
                None
            continue

#Create a report of donors
def report(donors):
    #Separate name from numbers, then recombine into list
    person = donors[::2]
    don = donors[1::2]
    for i in range(len(person)):
        don[i].insert(0, person[i])
    don.sort(key = len)
    don.reverse()
    # Table formatting.
    print '{0:<20}     {1:^13}     {2:^19}     {3:^20}'.format('Name','Total Donated',
        'Number of Donations', 'Average per Donation')
    print '-' * 91
    # Calculate report.
    for do in don:
        name = do[0]
        do.pop(0)
        print '{0:<20}     {1:^13}     {2:^19}     {3:^20}'.format(name,
            sum(do), len(do), sum(do)/len(do))
    return donors

if __name__ == '__main__':
    main_menu()
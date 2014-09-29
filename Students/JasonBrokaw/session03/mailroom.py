#!/usr/local/bin/python

donor_history = [(u"Colonel Mustard", [100, 200, 300])]
donor_history.append((u"Mrs. White", [50, 10.95]))
donor_history.append((u"Professor Plum", [300, 300]))
donor_history.append((u"Mr. Green", [1000, 2000]))
donor_history.append((u"Miss Scarlet", [1000]))

option_indexes = [1, 2, 3]
options = [u"Send a Thank You", u"Create a Report", u"Exit"]

def initial_prompt():
    """Return an int representing the user's selection among the options"""
    print u"Please select from the following options: "
    i = 0
    for index in option_indexes:
        print u"%i) %s" % (index, options[i])
        i = i + 1
    while True:
        try:
            selection = int(raw_input(u"Enter the number of your selection: "))
            break
        except ValueError:
            print u"I didn't understand that, please enter a number"

    if selection not in option_indexes:
        print u"Invalid selection\n\a"
        selection = initial_prompt()
    return selection

def list_donors():
    """List full names of donors"""
    print u"We have records for the following donors"
    for record in donor_history:
        print record[0]

def send_thankyou():
    """Generate a thank you note for an individual donor"""
    donor = raw_input(u"Enter the Full Name of the donor (or 'list' to list the donors, 'quit' to return to the main menu): ")
    if donor == u"list":
        list_donors()
        send_thankyou() #YIKES NOT SUPER HAPPY ABOUT THIS
        return
    if donor == u"quit":
        return

    for record in donor_history:
        if record[0] == donor:
            selected_record = record
            break
    else:
        selected_record = (donor, [])
        donor_history.append(selected_record)

    donation = raw_input(u"Enter the donation amount: ")

    while True:
        try:
            fdonation = float(donation)
            idonation = int(fdonation)
            if fdonation == idonation:
                donation = idonation
            else:
                donation = fdonation
            break
        except ValueError:
            print u"I didn't understand that, please enter a number."
            donation = raw_input(u"Enter the donation amount: ")

    selected_record[1].append(donation)

    print u"\n\n\n"
    print u"Dear %s:" % selected_record[0]
    print u"Thank you so much for your recent donation of $%.2f. This means so" % selected_record[1][-1]
    print u"much to the little orphaned children of Mr. Boddy, who recently perished"
    print u"in his own mansion under mysterious circumstances."
    print u"Sincerely,"
    print u"Orphan Relief International"
    print u"\n\n\n"

def create_report():
    print u"\n\n\n"
    donor_history.sort(key=lambda record: sum(record[1]))
    print u"%-20s%12s%8s%12s" % (u"Name", u"Total", u"No.", u"Avg.")
    for record in donor_history:
        total = sum(record[1])
        no = len(record[1])
        avg = float(total) / float(no)
        print u"%-20s%12.2f%8d%12.2f" % (record[0], total, no, avg)
    print u"\n\n\n"

if __name__ == '__main__':
    user_selection = initial_prompt()
    while user_selection != 3:
        if user_selection == 1:
            send_thankyou()
        if user_selection == 2:
            create_report()
        user_selection = initial_prompt()





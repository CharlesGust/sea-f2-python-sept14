#!/usr/bin/python

donation_DB = {
    "Alice": [500, 100, 100],
    "Betty": [50],
    "Carol": [1000, 10, 10],
    "Debbie": [25, 25, 25],
    "Ellie": [200, 200]
    }


def safe_input(prompt):
    """ get input, but silently handle common exceptions """
    try:
        return input(prompt)
    except (EOFError, KeyboardInterrupt):
        print
        return None


def safe_raw_input(prompt):
    """ get raw input, but silently handle common exceptions """
    try:
        return raw_input(prompt)
    except (EOFError, KeyboardInterrupt):
        print
        return None


def search_DB(full_name):
    """ search donation database, return None if name is not found """
    if full_name in donation_DB:
        return donation_DB[full_name]
    else:
        return None


def ask_Name():
    """ prompt the user for a name, or request for a list """
    global donation_DB

    while True:
        full_name = safe_raw_input("What is the Full Name?")
        if not full_name:
            continue
        elif full_name == "list":
            for donor in donation_DB:
                print donor
        else:
            if not search_DB(full_name):
                donation_DB[full_name] = []
            return full_name


def ask_Amount():
    """ prompt the user for a donation amount """
    while True:
        amount = safe_input("What is the donation amount?")
        if not amount:
            continue
        elif type(amount) != float and type(amount) != int:
            print "Please enter a number"
        else:
            return amount


def record_Donation(full_name, amount):
    donation_DB[full_name].append(amount)


def send_ThankYou():
    """ thanks donors for their gifts """

    full_name = ask_Name()
    amount = ask_Amount()
    record_Donation(full_name, amount)

    print "Dear %(donor)s, Thank you very much for your recent donation\
 of $%(amount).2f" % {"donor": full_name, "amount": amount}
    return


def create_Report():
    """ display formatted table of donation database """

    print "{0:20s} {1:5s} {2:7s}".format("Name", "Total", "Average")
    for donor in donation_DB:
        donor_name = donor
        if len(donor) > 20:
            donor_name = donor_name[0:17]+"..."
        total = sum(donation_DB[donor])
        average = total / len(donation_DB[donor])
        print "{0:20s} {1:5d} {2:7d}".format(donor_name,
                                             total,
                                             average)


def create_Letters():
    file_Prefix = "./Letters/"
    for donor in donation_DB:
        f = open(file_Prefix+donor, "w")
        letter = "Dear %(donor)s, Thank you very much for your donations totalling\
 $%(amount).2f".format({"donor": donor, "amount": sum(donation_DB[donor])})
        f.write(letter)
        f.close()
    print "Letters written to Letters directory"

main_menu_actions = {
    "1":    send_ThankYou,
    "2":    create_Report,
    "3":    create_Letters
}

if __name__ == "__main__":
    while True:
        action =\
            safe_raw_input("Choose: 1.Send Thank You, \
2.Create Report, 3.Write Letters: ")

        if not action:
            break
        elif action in main_menu_actions:
            main_menu_actions[action]()
        else:
            break

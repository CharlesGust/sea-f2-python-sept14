#!/usr/bin/python

donation_DB = [["Alice", [500, 100, 100]],
               ["Betty", [50]],
               ["Carol", [1000, 10, 10]],
               ["Debbie", [25, 25, 25]],
               ["Ellie", [200, 200]]]


def search_DB(full_name):
    """ search donation database, return None if name is not found """
    global donation_DB

    for donor in donation_DB:
        if donor[0] == full_name:
            return donor
    return None


def ask_Name():
    """ prompt the user for a name, or request for a list """
    global donation_DB

    while True:
        full_name = raw_input("What is the Full Name?")
        if full_name == "list":
            for donor in donation_DB:
                print donor[0]
        else:
            if not search_DB(full_name):
                donation_DB.append([full_name, []])
            return full_name


def ask_Amount():
    """ prompt the user for a donation amount """
    while True:
        amount = input("What is the donation amount?")
        if type(amount) != float and type(amount) != int:
            print "Please enter a number"
        else:
            return amount


def record_Donation(full_name, amount):
    global donation_db

    for donor in donation_DB:
        if donor[0] == full_name:
            donor[1].append(amount)
            return
    else:
        """ if name previously inserted when not found, name will be found """
        assert(False)
        donation_DB.append([full_name, [amount]])


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
        donor_name = donor[0]
        if len(donor[0]) > 20:
            donor_name = donor_name[0:17]+"..."
        print "{0:20s} {1:5d} {2:7d}".format(donor_name,
                                             sum(donor[1]),
                                             sum(donor[1])/len(donor[1]))
    pass

if __name__ == "__main__":
    while True:
        action = raw_input("Choose: 1. Send a Thank You, 2. Create a Report: ")

        if int(action) == 1:
            send_ThankYou()
        elif int(action) == 2:
            create_Report()
        else:
            break

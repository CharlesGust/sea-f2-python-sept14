donation_db = [["Alice", [500, 100, 100]],
               ["Betty", [50]],
               ["Carol", [1000, 10, 10]],
               ["Debbie", [25, 25, 25]],
               ["Ellie", [200, 200]]]


def send_Thank_You():
    full_name = raw_input("What is the Full Name?")
    if full_name == "list":
        for donor in donation_db:
            print donor[0]
    elif full_name not in donation_db:
        donation_db += [full_name]
    ask_amount = True
    while ask_amount:
        amount = raw_input("What is the donation amount?")
        if type(amount) == float or type(amount) == int:
            ask_amount = False
        else:
            print "Please enter a number"
    donation_db[full_name][1] += amount
    print "Dear %(donor)s, Thank you very much for your recent donation\
    of %(amount)i" % {"donor": full_name, "amount": amount}


def create_report():
    pass

if __name__ == "__main__":
    ask_action = True
    while ask_action:
        action = raw_input("Choose: 1. Send a Thank You, 2. Create a Report: ")

        if int(action) == 1:
            send_Thank_You()
        elif int(action) == 2:
            create_report()
        else:
            ask_action = False

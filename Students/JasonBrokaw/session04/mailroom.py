#!/usr/local/bin/python
import io, textwrap

donor_history = {u"Colonel Mustard": [100, 200, 300]}
donor_history[u"Mrs. White"] = [50, 10.95]
donor_history[u"Professor Plum"] = [300, 300]
donor_history["Mr. Green"] = [1000, 2000]
donor_history["Miss Scarlet"] = [1000]
def donorssort((i, donations)):
    return sum(donations)



def safe_input(prompt_string):
    """Returns user input, None if ^C or ^D"""
    try:
        response = raw_input(prompt_string)
    except (KeyboardInterrupt, EOFError):
        response = None
    return response

def list_donors():
    """List full names of donors"""
    print u"We have records for the following donors"
    for key in donor_history:
        print key

def generate_letter(donor, amount):
    """Return a letter (string) given a dict containing a name and a donation"""
    output = u"Dear {donor}:\n"
    output = output + textwrap.fill(u"Thank you so much for your recent donation of ${donation:.2f}. This means so much to the little orphaned children of Mr. Boddy, who recently perished in his own mansion under mysterious circumstances.")
    output = output + u"\nSincerely,\nOrphan Relief International"
    return output.format(donor=donor, donation=amount)

def send_thankyou():
    """Generate a thank you note for an individual donor"""
    donor = safe_input(u"Enter the Full Name of the donor (or 'list' to list the donors, 'quit' to return to the main menu): ")
    if donor == u"list":
        list_donors()
        send_thankyou() #YIKES NOT SUPER HAPPY ABOUT THIS
        return
    if donor == u"quit":
        return

    if not donor_history.has_key(donor):
        donor_history[donor] = []

    donation = safe_input(u"Enter the donation amount: ")

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
            donation = safe_input(u"Enter the donation amount: ")

    donor_history[donor].append(donation)
    print u"\n\n\n"
    print generate_letter(donor, donation)
    print u"\n\n\n"

def create_report():
    print u"\n\n\n"
    donor_history_list = donor_history.items()
    donor_history_list.sort(key=donorssort)
    print u"%-20s%12s%8s%12s" % (u"Name", u"Total", u"No.", u"Avg.")
    for record in donor_history_list: #Could have this use the dict, but I don't see why
        total = sum(record[1])
        no = len(record[1])
        avg = float(total) / float(no)
        print u"%-20s%12.2f%8d%12.2f" % (record[0], total, no, avg)
    print u"\n\n\n"

def write_letters():
    filename_format = u"{name}_{num:03d}_thankyou.txt"
    for key in donor_history:
        for donation, i in zip(donor_history[key], range(len(donor_history[key]))):
            letter_filename = filename_format.format(name=key.replace(' ', '_'), num=i+1)
            letter_file = io.open(letter_filename, 'w')
            letter_file.write(generate_letter(key, donation))
            letter_file.close()



options = {1: (u"Send a Thank You", send_thankyou), 2: (u"Create a Report", create_report), 10: (u"Exit",u"quit")}
options[3] = (u"Write a Full Set of Letters to Files", write_letters)
def optionsort((i, str)):
    return i

def initial_prompt():
    """Return an int representing the user's selection among the options"""
    print u"Please select from the following options: "
    option_list = options.items()
    option_list.sort(key=optionsort)
    for index, desc in option_list:
        print u"%i) %s" % (index, desc[0])
    while True:
        try:
            selection = int(safe_input(u"Enter the number of your selection: "))
            break
        except (ValueError, TypeError):
            print u"I didn't understand that, please enter a number"

    if selection not in options:
        print u"Invalid selection\n\a"
        selection = initial_prompt()
    return selection

if __name__ == '__main__':
    user_selection = initial_prompt()
    while options[user_selection][1] != 'quit':
        options[user_selection][1]()
        user_selection = initial_prompt()


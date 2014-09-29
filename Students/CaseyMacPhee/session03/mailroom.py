#!/usr/bin/env python

import random
import pprint
import io
dreamDonors = {'Bill Gates':[random.randint(500000, 1000000)],\
     'Leroy Hood': [random.randint(500000, 1000000)], 'Paul Allen': [random.randint(500000, 1000000)], 'Bill Ruckelshaus':\
      [random.randint(500000, 1000000), random.randint(500000, 1000000), random.randint(500000, 1000000)], 'Nathan Myhrvold':\
      [random.randint(500000, 1000000), random.randint(500000, 1000000)]}

def safe_input(inputphrase):
    useroutput = ""
    try:
        useroutput = raw_input(inputphrase)
    except EOFError:
        useroutput = None
    except KeyboardInterrupt:
        useroutput = None

    return useroutput

def mainPrompt():
    """Prints the main prompt"""
    s = """What would you like to do?

        -type 'p' to print report
        -type 's' to send a thank you
        -type 'q' to quit 
        -type 'd' to delete donor from list\n: """

    userresponse = safe_input(s)
    while userresponse != 'p' and userresponse != 's' and userresponse != 'q' and userresponse != 'd':
        userresponse = safe_input("Please type either 'p', 's','q', 'd'")


    return userresponse

def printAll():

    for i in dreamDonors:

        content = unicode(printThankYou(i, dreamDonors.get(i)[-1]))
        filename = "./" + i + ".txt"
        print "Writing file name: ", filename
        outfile = io.open(filename, 'w')
        outfile.write(content)
        outfile.close()

def donor():
    prompt = "Would you like a list of current donors? (type 'list') or...\n\
Enter a new donor name (full name) or...\n\
Print thank you's for entire list? (type 'print all')\n: " 

    donorName = safe_input(prompt)
    

    if donorName == "print all":
        print "got to the print all call"
        printAll()
    elif donorName == "list":
        pp = pprint.PrettyPrinter(indent=4)
        pp.pprint(dreamDonors.keys())
    else:
        amount = safe_input("And for what amount?\n: ")
        while not amount.isalnum():
            amount = safe_input("Please enter a number value")
        
        donation = int(amount)
        inlist = False

        for name in dreamDonors:
            if donorName == name:
                dreamDonors.get(name).append(donation)
                inlist = True
        if inlist == False:
            dreamDonors[donorName] = [donation]

        answer = safe_input("Would you like to print a thank you? (type 'y' for yes or 'n' for no)\n: ")
        if  answer == 'y':
            printThankYou(donorName, donation)
   

def printThankYou(name,amount):

    firstname, lastname = name.split(" ")

    letterformat = """
Dear {},
Our sincerest thanks for your contribution to our cause. Your donation of ${:,} will undoubtably be\
an integral part of our success in the coming year. We expect it to be a difficult road ahead,\
but we truly derive strength from, and are encouraged by the outpouring of generosity from donors\
like yourself. Feel free to subscribe to our mailing list, or check out our blog to follow our\
progress, and to see your dollars in action. Expect a gift from us in the mail soon- just a\
small token of our gratitude, and a way to show others your continued support of our efforts.
Thank you again, from all of us here.
"""

    #print letterformat.format(firstname, amount)
    return letterformat.format(firstname, amount)
    
def deleteDonor():
    print "Who would you like to delete from the list?"
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(dreamDonors.keys())
    print "\n"

    answer = safe_input("Type the name exactly as it appears, or 'b' to go back\n: ")
    try:
        if answer != 'b':
            try:
                dreamDonors.pop(answer)
            except:
                print "That name does not match anyone in the list"
    except:
        print "\n"

def report():
    statlist = []
    for i in dreamDonors:
        totaldonations = sum(dreamDonors.get(i))
        number = len(dreamDonors.get(i))
        average = totaldonations/number
        newentry = (i,totaldonations,number,average)
        statlist.append(newentry)
        statlist.sort(key=getKey, reverse=True)

    for person in range(len(statlist)):
        print "Name: {}\tCumulative: {:,}\tNumber of Donations: {:,}\tAverage: {:,}"\
        .format(statlist[person][0],statlist[person][1],statlist[person][2],statlist[person][3])
    
    print "\n"
def getKey(item):
    return item[1]

if __name__ == '__main__':
    
    while True:

        response = mainPrompt()

        if response == 'q':
            break
        elif response == 's':
            donor()
        elif response == 'p':
            report()
        elif response == 'd':
            deleteDonor()


    

        

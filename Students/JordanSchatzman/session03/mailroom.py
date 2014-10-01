#!/usr/bin/env python
import sys
import codecs


donors = {u"Richard Sherman":[16,213,3],u"Kam Chancellor":[1000,2000,3000],
          u"Marshawn Lynch":[200, 500],u"Russell Wilson":[10000,30000,40000],
          u"Percy Harvin":[2345,123,6543]}
    
    
def SelectTask():
    """This is the first prompt the user will see"""
    FirstInput=raw_input(u"Enter 'Send a Thank You' or 'Create a Report' or 'exit' to exit the program: ")
    if FirstInput == "Send a Thank You":
        ThankYou()
    elif FirstInput == "Create a Report":
        CreateReport()
    elif FirstInput == "exit":
        sys.exit()
        
        
def ThankYou():
    """This function determines the logic flow if the user wants to send a thank you note"""
    global ThankInput
    ThankInput = raw_input(u"Enter full name of donor or 'list' to see list of all donors or enter 'restart' to return to original prompt: ")
    if ThankInput == "list":
        print donors.keys()
        ThankYou()
    elif ThankInput not in donors.keys() and ThankInput != "restart":
        AddDonor()
    elif ThankInput in donors.keys():
        CurrentDonor()
    elif ThankInput == "restart":
        SelectTask()

def AddDonor():
    """This functuion adds a donor if the user inputs a value not already in the list of donors"""
    AddDonorAmount = raw_input(ThankInput + u" has been added to the list, please enter his/her donation amount or enter 'restart' to restart program: ")
    if AddDonorAmount == 'restart':
        SelectTask()
    else:
        try:
            float(AddDonorAmount)
            donors.update({ThankInput:[AddDonorAmount]})
            print "Thank you, " + ThankInput + " for your kind contribution of " + AddDonorAmount + " dollars, you are an incredible person and a great player, Go Hawks!"
        except ValueError:
            print "Please enter a number"
            AddDonor()
        

def CurrentDonor():
    """The function promtps the user to add a donation amount for a preexisting donor"""
    AddDonorAmount2 = raw_input("How much did this donor donate: ")
    if AddDonorAmount2 == "restart":
        SelectTask()
    else:
        try: 
            float(AddDonorAmount2)
            donors.get(ThankInput).append(AddDonorAmount2)
            print "Thank you, " + ThankInput + " for your kind contribution of " + AddDonorAmount2 + " dollars, you are an incredible person and a great player, Go Hawks!"
        except ValueError:
            print "Please enter a number"
            CurrentDonor()
    


def CreateReport():
    """Print list of donors, sorted by total historical donation amount"""
    print u" Name     | Total Donated |             # of Donations       | Average Donation"
    print u"=" * 75
    for a,b in donors.items():
        Name = a
        DonationSum = sum(b[:])
        NumDonations = len(b[:])
        Average = DonationSum / NumDonations
        indent1 = u" " * (32 - (len(Name) + len(str(DonationSum))))
        indent2 = u" " * (42 - (len(Name) + len(indent1) + len(str(DonationSum))))
        indent3 = u" " * (65 - (len(Name) + len(indent1) + len(str(DonationSum)) + \
                            len(indent2) + len(str(NumDonations)) + len(str(Average))))
        print Name, indent1, DonationSum, indent2, NumDonations, indent3, Average
        print u"=" * 75


def CreateFile():
    """This function will create a file in the local directory for thanking each donor for his/her donation"""
    for a,b in donors.items():
        name = a
        donationsum = sum(b[:])
        thanksfilecontent = "Thank you, " + name + " for your kind contributions of " + str(donationsum) + " dollars, you are an incredible person and a great player, Go Hawks!"
        filename = (u"{name}.txt").format(name=name)
        f = codecs.open(filename, 'w')
        f.writelines(thanksfilecontent)
        f.close()

   

if __name__ == "__main__":
    CreateFile()
    SelectTask()
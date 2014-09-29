#!/usr/env/python
choose = ''
donors = {'Kevin':[100, 200, 300], 
          'Chris':[300, 300, 400], 
          'John':[300], 
          'Paul':[400, 500], 
          'Nick':[700]}

def mailroom(choose, donors):

    while choose != str(1) or choose != str(2):
        choose = raw_input("Select 1 to 'Send a thank you' or 2 to" 
            + " 'Create a report': ")

        if choose == str(1) or choose == str(2):
            break
        elif choose == 'quit':
            break
        else:
            print "Select either 1 or 2."

    while choose == str(1):
        send_to = raw_input("Who would you like to send a thank you to?: ")

        if send_to == 'quit':
            break

        if send_to == 'list':
            for key in donors:
                print key
            send_to = raw_input("Send thank you to: ")

        if send_to in donors:
            donation = input("Donation amount: ")
            donors[send_to].append(donation)

        if send_to not in donors:
            donation = input("Donation amount: ")
            donors[send_to] = [donation]

        historic = sum(donors[send_to])
        print ("Thank you %s for your generous donation of $%d. We"
                " really appreciate it. Total donation to date: %d"
                %(send_to, donation, historic))
        mailroom(choose, donors)
        break

    while choose == str(2):
        sort_list = []
        for donor in donors:
            sort_list.append([donor,
                             sum(donors[donor]),
                             len(donors[donor]),
                             sum(donors[donor])/len(donors[donor])])
        sort_list.sort(key=lambda x: x[1], reverse=True)
        for i in sort_list:
            print ("Name:%s, Total:%i, # of donations:%i, Avg:%i" 
                    % (i[0], i[1], i[2], i[3]))
        mailroom(choose, donors)
        break
    
    while choose == 'quit':
        break


mailroom(choose, donors)

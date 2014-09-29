#this program will keep me from typing out a bunch of thankyou notes

doners = dict(Jon=[100,200,300], Mike=[20,234,443], Kele=[113,420], Emily=[4,33,56], Rachel=[45,65,87])
print doners

def MainMenu():
	display = raw_input("Would you like to 'Send a Thank You' or 'Create a Report'. You can also type 'list' for a report of names. Or type (Q) to quit. ")
	if display[0].lower() == "l":
		for key in doners:
			print (key)
	while display[0].lower() == "s":
		name = raw_input("Who would you like to send a thank you card to? Please type a name, or type 'l' for a list of names to choose from.")
		if name[0].lower() == "l":
			for key in doners:
				print (key)
		while doners.has_key(name) is True:
			d_amt = raw_input("Which donation amount would you like to thank them for? Type (back) to return to previous menu.")
			if d_amt[0].lower() == "b":
				break
			try:
	  			val = int(d_amt)
	  			if not d_amt in doners:
	  				doners.setdefault(name, []).append(d_amt)
	  				print "Thank you %s for your donation of $%i." % (name, val)
	  				MainMenu()
	  			else:
	  				MainMenu()
	  				
			except ValueError:
			   print("Please enter a number")
			continue


			
	while display[0].lower() == "c":
		reports = []
		for (name, donation) in doners.items():
			total = round(sum(donation))
			number = len(donation)
			av_gift = round(total / number, 2)
			reports.append( (name, total, number, av_gift) )
			print repr(name)
			print repr(total)
			print repr(number)
			print repr(av_gift)

		return False




if __name__ == '__main__':
	MainMenu()	


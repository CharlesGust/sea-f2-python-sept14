def safe_input(inputphrase):
	useroutput = ""
	try:
		useroutput = raw_input(inputphrase)
	except EOFError:
		useroutput = None
	except KeyboardInterrupt:
		useroutput = None

	return useroutput

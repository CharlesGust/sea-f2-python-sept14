import os

oldfilepath = raw_input("What is the absolute path of the file you'd like to copy?\n: ")


newdirpath = raw_input("""What is the path of the directory you would like to copy to?
	(if blank, the file will be saved to the current working directory)\n: """)

if newdirpath == None:
	newdirpath = os.getcwd()

newfilename = raw_input("What's the name of your new copied file?")

fullpath = os.path.join(newdirpath, newfilename)

oldfile = open(oldfilepath, 'r')
oldtext = oldfile.read()

oldfile.close()
newfile = open(fullpath, 'w')
newfile.write(oldtext)
newfile.close()

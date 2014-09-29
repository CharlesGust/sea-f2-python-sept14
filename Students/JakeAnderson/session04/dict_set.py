#create dictionary
random_stuff = dict(name='Chris', city='Seattle', cake='Chocolate')
print random_stuff
#lose the cake
random_stuff.pop("cake")
print random_stuff
#add the fruit
random_stuff['fruit'] = 'Mango'
print random_stuff
#check for the none existant cake
if 'cake' in random_stuff:
	print "Its a Ghost!!"
else: print "The baker is out of a job."
#doublecheck mango made it in the mix
if 'Mango' in random_stuff.values():
	print "We're all healthy up in this shiiz."
else: print "No one will ever read this."
#create a dictionary of numbers between 0 and 15
keys = []
values = []
for i in range(15) :
    keys.append(i)
    values.append(hex(i))
    #zip the dict after they have been hexed
d1 = dict(zip(keys, values))
keys = random_stuff.keys()
print d1

new_random_stuff = {}

for key,value in random_stuff.iteritems():
	new_random_stuff[key] = value.count('a')

print new_random_stuff

s2 = set([0,2,4,6,8,10,12,14,16,18,20])
s3 = set([0,3,6,9,12,15,18,])
s4 = set([0,4,8,12,16,20])

print s2
print s3
print s4

print s3.issubset(s2)
print s4.issubset(s2)

pyth = set("pythoni")
marth = frozenset(("marathon"))
print pyth.union(marth)
print pyth.intersection(marth)




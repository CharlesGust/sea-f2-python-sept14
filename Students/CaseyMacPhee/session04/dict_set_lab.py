
Chris = {'name': 'Chris', 'city': 'Seattle', 'cake': 'Chocolate'}
print Chris
Chris.pop('cake')
print Chris
Chris['fruit'] = 'Mango'
print Chris
print Chris.keys()
print Chris.values()
'cake' in Chris
'Mango' in Chris.values()

intUni = {}
l1 = range(16)
l2 = []
for i in l1:
	l2.append(hex(i))

for h, j in zip(l1, l2):
	intUni[h] = j

print intUni

newdict = {}

for l in Chris:
	count = 0
	value = Chris.get(l)
	for letter in value:
		if letter == 'a' or letter == 'A':
			count += 1

	newdict[l] = count
print newdict

div2 = set()
div3 = set()
div4 = set()

q = range(21)

for i in q:
	if i % 2 == 0:
		div2.update([i])
	if i % 3 == 0:
		div3.update([i])
	if i % 4 == 0:
		div4.update([i])
print div2
print div3
print div4
print div3.issubset(div2)
print div4.issubset(div2)

python = set()

for i in 'python':
	python.update([i])
print python
python.update(['i'])
print python

tuplekey = ()
for j in 'marathon':
	tuplekey = tuplekey + (j,)
marathon = frozenset(tuplekey)
print marathon

print marathon.union(python)
print marathon.intersection(python)










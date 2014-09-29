#!/usr/bin/python
# -*- coding: latin-1 -*-
import os, sys
import random
import io

sherlock = io.open('sherlock.txt', mode='r')

#iterater startes at actual start of book, skipping intro stuff
for i in range(61):
	sherlock.readline()

#save all text after header and table of contents to "source"
source = sherlock.read()
sherlock.close()

source = source.split()


source_sher = {}

for i in range(len(source)-2):
	source_sher.setdefault("%s %s" % (source[i], source[i+1]),[])\
	.append(source[i+2])

trigram = ["This", "is"]


for i in range(100):
	joined = (" ").join(trigram[-2:])
	r = random.randint(0, len (source_sher.get(joined))-1)

	if source_sher.get(joined):
		trigram.append(source_sher.get(joined)[r])

print(" ").join(trigram)
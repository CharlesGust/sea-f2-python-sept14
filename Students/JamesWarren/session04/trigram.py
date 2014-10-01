#!/usr/bin/env python
import random
import io

sherlock = io.open('sherlock.txt', mode='r')

#iterator skips header and table of contents at beginning of file
for i in range(61):
    sherlock.readline()

#save all text after header and table of contents to "source"
source = sherlock.read()
sherlock.close()

source = source.replace("--", ", ")
source = source.split()

source_dict = {}

#loops through text, creates dictionary sets of "word1 word2 : word3"
for i in range(len(source)-3):
    source_dict.setdefault("%s %s" % (source[i], source[i+1]), [])\
    .append(source[i+2])

trigram = ["This", "is"]


for i in range(250):
    joined = (" ").join(trigram[-2:])
    r = random.randint(0, len(source_dict.get(joined))-1)
    #if last two words of trigram match key in source_dict
    if source_dict.get(joined):
        #append the first value to the trigram
        trigram.append(source_dict.get(joined)[r])


print (" ").join(trigram) + "..."
#!/usr/local/bin/python

import urllib
import random, textwrap


base_text_file = urllib.urlopen(u"http://codefellows.github.io/sea-c15-python/_downloads/sherlock.txt")

base_text = base_text_file.read()

base_text_file.close()


base_list = base_text.split()

trigrams = {} #Each key will be a pair of words, and the value will be a list of words that follow that pair

key_length = 2

for i in range(len(base_list) - key_length):
    key = " ".join(base_list[i:i+key_length])
    if trigrams.has_key(key):
        trigrams[key].append(base_list[i+key_length])
    else:
        trigrams[key] = [base_list[i+key_length]]


default_key = " ".join(base_list[267:267+key_length]) #This starts at "world has seen but as a lover ..."

def generate_text(length=500, starting_key=default_key):
    if not trigrams.has_key(starting_key):
        starting_key = default_key
        print "That is not a valid key, using '" + starting_key + "'"
    output = starting_key.split() #build this up as a word list
    key = starting_key
    for i in range(length):
        output.append(random.sample(trigrams[key],1)[0])
        key = " ".join(output[-key_length:])
    print textwrap.fill(" ".join(output))

if __name__ == '__main__':
    generate_text()

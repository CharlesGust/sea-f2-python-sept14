#!/usr/bin/env python
import codecs
from io import open
import sys
import string
import random

def trigram(in_file):
    """create trigram given input text file"""
    #open and process the text file
    file = codecs.open(in_file)
    file_text = file.read()
    file_words = file_text.split()
    words = []
    for word in file_words:
        words.append("".join(c for c in word if c.isalpha()).lower())
    trigram_dict = {}
    #create trigram dictionary
    for i in range(len(words)-2):
        keys = '%s %s' % (words[i], words[i + 1])
        trigram_dict.setdefault(keys, []).append(words[i + 2])
    print trigram_dict
if __name__ == "__main__":
    trigram('sherlock.txt')
    

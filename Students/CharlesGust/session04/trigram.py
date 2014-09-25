#! /usr/bin/python

import string
import codecs
import random

trigram = {}
# CMGTODO: balance ()[]{}<> delimiters
delimiters = "\"'"
char_count = {}

def any_delimiters(word):
    for c in delimiters:
        if word[0] == c or word[-1] == c:
            return True
    return False


def process_tokens(token_list):
    global trigram

    word_index = 0
    word = ["", "", ""]
    for w in token_list:
        if w == "\n":
            continue
        word[word_index % 3] = w
        if word_index > 1:
            """
            # the folowing line would store the keys in one case
            if word_index > 0:
                word[(word_index-1) % 3] = word[(word_index-1) % 3].upper()
            """
            key = "%s %s" %\
                (word[(word_index-2) % 3], word[(word_index-1) % 3])
            if not trigram.get(key):
                trigram[key] = []

            # intentionally permit duplicate values to increase chances
            # based on frequency of use
            trigram[key].append((w, any_delimiters(w)))
        word_index += 1

"""
def string_remove(s, chars):
    for c in chars:
        loc = string.find(s, c)
        s = "%s%s" % (s[:loc], s[loc+1:])
    return s
"""

def populate_dictionary():
    """
    sep = string.punctuation+string.whitespace+" "+"\n"+"\r"

    # remove apostrophe and dash as a word delimiters
    sep = string_remove(sep, "'-")
    """

    f = open("Sherlock.txt", mode="r")

    # from stackoverflow.com/questions/836219
    file_contents = f.read()
    begin_pos = file_contents.find("*** START OF THIS PROJECT GUTENBERG EBOOK")

    if begin_pos > 0:
        begin_pos = file_contents.find("***", begin_pos+1)

        if begin_pos > 0:
            file_contents = file_contents[begin_pos:]

    end_pos = file_contents.rfind("*** END OF THIS PROJECT GUTENBERG EBOOK")
    if end_pos > 0:
        file_contents = file_contents[:end_pos]

    token_list = file_contents.split()
    process_tokens(token_list)

"""
def select_word(val_list):
    tries = 0
    while tries < len(val_list):
        index = random.randint(0, len(val_list)-1)
        word = val_list[index][0]

        if not val_list[index][1]:
            return word
        else:
            # check for unbalanced delimiter
            for c in delimiters:
                if char_count[c] % 2 == 0:
                    if word[0] == c:
                        char_count[c] += 1
                        return word
                else:
                    if word[:-1] == c:
                        char_count[c] += 1
                        return word
        tries += 1
    return None
"""


def select_word(val_list):
    index = random.randint(0, len(val_list)-1)
    word = val_list[index][0]
    slice_beg = False
    slice_end = False

    if val_list[index][1]:
        for c in delimiters:
            if char_count[c] % 2 == 1:
                if word[0] == c:
                    slice_beg = True
                else:
                    char_count[c] += 1
            else:
                if word[-1] == c:
                    slice_end = True
                else:
                    char_count[c] += 1

    return (word, slice_beg, slice_end)


def balance_quote(word):
    ret_val = word[0]
    if word[1]:
        ret_val = ret_val[1:]
    if word[2]:
        ret_val = ret_val[:-1]
    return ret_val


def generate_story():
    for c in delimiters:
        char_count[c] = 0

    # from http://stackoverflow.com/questions/4859292
    next_word = random.choice(list(trigram.keys()))
    print next_word.capitalize()

    while True:
        third_val_list = trigram.get(next_word)
        if not third_val_list:
            break
        third_word_tuple = select_word(third_val_list)
        """
        if not third_word:
            break
        """
        assert(third_word_tuple[0])

        print balance_quote(third_word_tuple),
        next_word = next_word.split()[1] + " " + third_word_tuple[0]


if __name__ == "__main__":
    populate_dictionary()
    generate_story()

#!/usr/bin/env python2.7
import random

def trigrams():

    texts = ''

    print 'Enter text for triagram analysis: '

    #Can only be done with continuous lines (not paragraphs)
    while True:
        line = raw_input()
        if not line:
            break
        texts += line + ' '

    ttexts = (texts.split(' '))
    result = list(ttexts)
    ltexts = list(ttexts)
    del result[0:2]

    for i in range(len(ltexts) - 1):
        ltexts[i] = ltexts[i] + " " + ltexts[i + 1]

    ltexts.pop()
    ltexts.pop()

    # print ltexts
    # print result

    dtexts = {}
    for i in range(len(ltexts)):
        #print ltexts[i], dtexts.keys()
        if ltexts[i] in dtexts.keys():
            dtexts[ltexts[i]].append(result[i])
        else:
            dtexts[ltexts[i]] = [result[i]]
        #print dtexts


    # START OF TRIGRAM DICTATION
    start = random.choice(dtexts.keys())
    print start
    end = random.choice(dtexts.get(start))  #Gets a random choice within value list
    print end

    rewrite = ''
    rewrite = (start + ' ' + end)
    print rewrite


    lasttwo = (rewrite.split(' '))[1:]  # Puts 3 words into a list
    lasttwo = lasttwo[0] + ' ' + lasttwo[1]  # Consolidates last 2 items in list


    while len(rewrite) < 2000:
        if lasttwo in dtexts.keys():
            end = random.choice(dtexts.get(lasttwo))
            rewrite += ' ' + end
            # print rewrite
            lasttwo = (rewrite.split(' '))
            lasttwo = lasttwo[len(lasttwo) - 2:]
            lasttwo = lasttwo[0] + ' ' + lasttwo[1]
        elif lasttwo not in dtexts.keys():
            dtexts[lasttwo] = random.choice(dtexts.values())
        else:
            break


    print rewrite








#    .replace() # for replacing it with whitespace


if __name__ == '__main__':
    trigrams()


    # Use split to separate text (how do you do it with punctuation?)
    # Combine 2 consecutive strings into a single item, key
    # Identify third item as a value for the key (separate structures and zip, )
    # Use for loop to setup dictionary
    # Use if statement to add new splices to dictionary

    # a piece of pie for a piece that's rare
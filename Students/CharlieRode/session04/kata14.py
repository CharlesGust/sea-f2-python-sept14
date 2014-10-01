#!/usr/bin/env python
import io, urllib2, random

def two_words(l):
    """Takes a list l= [l0, l1, l2, ...] and returns a new list of key value pairs, (a, b), where\
    a= "li l(i+1)", and b= [l(i+2)]"""
    k= []
    for i in range(len(l) -2):
        k.append(((u' '.join(l[i:i+2])), [l[i+2]]))
    return k

def build_paragraph(d):
    p= []
    for i in range(random.randint(3, 8)):
        p.append(build_line(d))
    return u' '.join(p) + '\n\n'

def build_line(d):
    first_three= random.choice(d.keys())
    first_three+= u' '+ d[first_three][0]
    
    words= first_three.split(u' ')

    for i in range(random.randint(3, 15)):
        try:
            key= u' '.join(words[-2:])
            words.append(d[key][random.randint(0, len(d[key]) - 1)])
        except KeyError:
            continue
    line= u' '.join(words) + u'.'
    return line.capitalize()
        

def strip_punct(s):
    punct= [u'.', u',', u"'", u'?', '!', ';', '\n', u'"']
    result= []
    for c in s:
        if c not in punct:
            result.append(c)
    return u''.join(result)

def build_dict(lines):
    d= {}
    for line in lines[:2000]:
        line= strip_punct(line)
        stage= two_words(line.split(u' '))
        for k, v in stage:
            if k in d.keys():
                d[k] += v
            else:
                d[k]= v
    return d




if __name__ == '__main__':

    result = urllib2.urlopen('http://codefellows.github.io/sea-c15-python/_downloads/sherlock.txt')
    sherlock_holmes= result.read().decode("utf-8")
    result.close()

    sh= 'Sherlock_Holmes.txt'
    open(sh, 'a').close()

    f= io.open(sh, 'r+')
    f.write(sherlock_holmes)

    f.seek(0)
    lines= f.readlines()[122: 25358: 2]
    f.close()

    tridict= build_dict(lines)
    
    p= io.open('trigram_story.txt', 'w')
    for i in range(5):
        p.write(build_paragraph(tridict))
    p.close()
    





          
        





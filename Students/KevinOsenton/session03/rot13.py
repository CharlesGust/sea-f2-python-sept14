#!/usr/env/python
def rot13(text):
    lower_alphabet = 'abcdefghijklmnopqrstuvwxyz'
    upper_alphabet = lower_alphabet.upper()

    modify = ''
    for char in text:
        if char in lower_alphabet:
            modify += lower_alphabet[(lower_alphabet.index(char)+13)%26]
        elif char in upper_alphabet:
            modify += upper_alphabet[(upper_alphabet.index(char)+13)%26]
        else:
            modify += char
    return modify

if __name__ == '__main__':
    assert rot13(rot13("Hello World")) == "Hello World"
    assert rot13(rot13("My name is Kevin")) == "My name is Kevin"
    assert rot13(rot13("codefellows")) == "codefellows"
    print "All tests complete"
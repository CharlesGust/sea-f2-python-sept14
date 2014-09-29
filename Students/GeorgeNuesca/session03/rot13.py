#!/usr/bin/env python2.7

def rot13(text):
    text = list(text)
    for i, t in enumerate(text):
        # ROT13 for lower case letters
        if ord(t) in range(ord('a'), ord('z') + 1):
            if (ord(t) + 13) > ord('z'):
                text[i] = chr(12 - abs(ord('z') - ord(t)) + ord('a'))
            else:
                text[i] = chr(ord(t) + 13)
        # ROT13 for upper case letters
        elif ord(t) in range(ord('A'), ord('Z') + 1):
            if (ord(t) + 13) > ord('Z'):
                text[i] = chr(12 - abs(ord('Z') - ord(t)) + ord('A'))
            else:
                text[i] = chr(ord(t) + 13)
        # Pass all other characters
        continue
    text = ''.join(text)
    return text

# Try with "translate" Built-in

if __name__ == '__main__':
    assert rot13('abcdefghijklm nopqrstuvwxyz') == 'nopqrstuvwxyz abcdefghijklm'
    assert rot13('ABCDEFGHIJKLM NOPQRSTUVWXYZ') == 'NOPQRSTUVWXYZ ABCDEFGHIJKLM'
    assert rot13('`1234567890-=[]\;,./ ~!@#$%^&*()_+{}|:"<>?') == '`1234567890-=[]\;,./ ~!@#$%^&*()_+{}|:"<>?'
    assert rot13('We will go to Nishiki with George and Beth for #1 otoro.') == 'Jr jvyy tb gb Avfuvxv jvgu Trbetr naq Orgu sbe #1 bgbeb.'
    print 'TEST CASES PASS'

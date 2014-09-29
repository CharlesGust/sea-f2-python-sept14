def rot13(str):
    encryptedtxt = ''
    for char in xrange(len(str)):
        temp = str[char]
        if temp.isalpha():
            if temp.isupper():
                temp2 = ord(temp)
                temp2 += 13
                if temp2 > 96:
                    temp2 = 70 + (temp2 - 96)
                encryptedtxt += chr(temp2)
            else:
                temp2 = ord(temp)
                temp2 += 13
                if temp2 > 122:
                    temp2 = 96 + (temp2 - 122)
                encryptedtxt += chr(temp2)
        else:
            encryptedtxt += temp
    return encryptedtxt
if __name__ == '__main__':
    assert rot13('Hello') == 'Uryyb'
    x = 'This is a string with spaces, and punctuation.'
    assert rot13(x) == 'Guvf vf n fgevat jvgu fcnprf, naq chapghngvba.'
    print 'running'
import string

def rot13(str):
    """Return rot13 encryption of str"""
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lowercase_alphabet = alphabet.lower()
    encrypted_alphabet = alphabet[13:] + alphabet[0:13]
    encrypted_lowercase_alphabet = encrypted_alphabet.lower()
    encryption = string.maketrans(alphabet + lowercase_alphabet, encrypted_alphabet + encrypted_lowercase_alphabet)
    return str.translate(encryption)

if __name__ == '__main__':
    test_string = "Hello, world. Here is a test string. 1, 2; 3"
    assert test_string == rot13(rot13(test_string))
    assert rot13("A") == "N"
    assert rot13("a") == "n"
    assert rot13(" ?^%81") == " ?^%81"
    print "All Tests Pass"

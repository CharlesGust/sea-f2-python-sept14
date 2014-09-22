

def rot13(string):
    letters = [chr(i) for i in range(97, 123)] * 2
    upper_place = []
    for i in range(len(string)):
        if string[i].isupper(): upper_place.append(i)
    result = []
    for c in string.lower():
        if c in letters:
            result.append(letters[letters.index(c) + 13])
        else:
            result.append(c)
    result ="".join(result)
    for x in upper_place:
        result = capitalize_nth(result, x)
    return result

def capitalize_nth(s, n):
    return s[:n] + s[n:].capitalize()


if __name__ == "__main__":

    assert rot13("abcdefg") == "nopqrst"
    assert rot13("ABcdEfG") == "NOpqRsT"
    assert rot13("Charlie Rode") == "Puneyvr Ebqr"
    assert rot13("What the !@&# is that?") == "Jung gur !@&# vf gung?"

    print "All tests pass"
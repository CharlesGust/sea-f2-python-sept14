def rot13(str):
    return str.encode("ROT13")


def rot13_simple(str):
    str_rot13 = ""
    for i in range(0, len(str)):
        new_c = str[i]
        if str[i].isalpha():
            base = 'a' if str[i].islower() else 'A'
            new_c = chr(ord(base) + (ord(str[i]) - ord(base) + 13) % 26)
        str_rot13 = "%(current_s)s%(c)s" % \
            {"current_s": str_rot13, "c": new_c}
    return str_rot13


if __name__ == "__main__":
    user_input = raw_input("What would you like to ROT13?")
    assert(user_input == rot13(rot13(user_input)))
    assert(user_input == rot13(rot13_simple(user_input)))
    assert(user_input == rot13_simple(rot13(user_input)))
    assert(user_input == rot13_simple(rot13_simple(user_input)))
    print rot13(user_input)

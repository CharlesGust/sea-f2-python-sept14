#! /usr/bin/python


def safe_input(prompt):
    try:
        return raw_input(prompt)
    except (EOFError, KeyboardInterrupt):
        return None


if __name__ == "__main__":
    ret = safe_input("Would you like to type string, or Ctrl-C or Crtl-D?")
    print ret

#!/usr/bin/env python

def safe_input(message):
    try:
        userin = raw_input("%s" % message)
    except (EOFError, KeyboardInterrupt) as the_error:
        return None
    else:
        return userin

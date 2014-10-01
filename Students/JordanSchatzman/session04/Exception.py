#!/usr/bin/env python
import sys

    
def Safe_Input():
    """This is the first prompt the user will see"""
    try:
        Input=raw_input(u"Enter something to raise an error: ")
    except EOFError, KeyboardInterrupt:
        return None
    print Input
        
   

if __name__ == "__main__":
    Safe_Input()
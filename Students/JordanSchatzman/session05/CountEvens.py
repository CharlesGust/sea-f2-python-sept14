#!/usr/bin/env python
import os

def CountEvens(nums):
    return len([x%2 for x in nums if x%2 == 0])
    


if __name__ == '__main__':
    assert CountEvens([2, 1, 3, 6, 7, 10, 2, 5]) == 4
    assert CountEvens([2, 4, 6, 8]) == 4
    assert CountEvens([1, 3, 5, 7]) == 0
    

#!/usr/bin/env python


def the_list(n):
    return [lambda x, i = i: x + i for i in range(n)]



if __name__ == '__main__':
    the_list10 = the_list(10)
    assert the_list10[2](3) == 5
    assert the_list10[1](3) == 4
    assert the_list10[2](6) == 8
    assert the_list10[3](3) == 6
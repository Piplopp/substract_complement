#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    Use the 9s and 10s complement method to do substraction

    Method:
    A - B ==>
    We take the 10s of B: 9s complement + 1
    A + B then ignore final carry

    examples:

    A = 100
    B = 75
    B_comp = 7 --> 2 and 5 --> 4 = 24+1 = 25
    A + B_comp = 125
    ignore final carry: (1)25 ==> result is 25

    ---
    A = 100
    B = 300
        B        300
        B_comp   699+1 = 700
    A + B_comp = 800
    (no final carry here so the result is - the complement of that number)
    (final carry if max(len A, len B) <= len A+B_comp)
    800 complement --> 199+1 = 200
    add "-"
    A - B = -200
    ---
"""

# Import
import sys



#######
# run #
#######
if __name__ == "__main__":
    complement_table = {
        "0":"9", "1":"8", "2":"7", "3":"6", "4":"5",
        "5":"4", "6":"3", "7":"2", "8":"1", "9":"0"
    }

    # declare
    A               = str(sys.argv[1])  # number to substract to
    B               = str(sys.argv[2])  # number to substract
    B_complement    = ""                # 10s complement of B

    # add 0 to the left until the 2 string are the same length
    size = max(len(A), len(B))
    A = A.rjust(size, "0")
    B = B.rjust(size, "0")

    # 9s complement of B
    for i in B:
        B_complement += complement_table[i]

    # sum this; the + 1 is for ending B 10s complementation
    sum = int(A) + (int(B_complement) + 1)

    # if the ""substracted"" is lower than the "substractor"
    if int(B) > int(A):
        sum_complement = "" # 10s complement of sum
        for i in str(sum):
            sum_complement += complement_table[i]
        print("-"+str(int(sum_complement)+1)) # same as B
    else:
        print(str(sum)[-size:])
        # N.B. we could avoid this final -size by fixing the list length and
        # ignoring the overflowing "1"
        # but i'm a bit lazy...

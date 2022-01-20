#!/usr/bin/python3

import sys

def bin_to_dec(n):
    return int(n, 2)

def dec_to_bin(n):
    return bin(n).replace('0b', '')

if sys.argv[1] == '-d' or sys.argv[1] == '--decimal':
    decimal_number = int(input('Input a decimal number: '))
    print(dec_to_bin(decimal_number))

elif sys.argv[1] == '-b' or sys.argv[1] == '--binary':
    binary_number = input("Input a binary number: ")
    print(bin_to_dec(binary_number))

elif sys.argv[1] == '' or sys.argv[1] == 0:
    print('ERROR: Please specify shell parameter')

else:
    print('ERROR: Invalid parameter')
#! /usr/bin/python3

import sys, argparse

# TODO: Add functionality for binary to hex and hex to binary conversions
# TODO: Add input validation

hex_list = {
    "1" : "1",
    "2" : "2",
    "3" : "3",
    "4" : "4",
    "5" : "5",
    "6" : "6",
    "7" : "7",
    "8" : "8",
    "9" : "9",
    "10" : "A",
    "11" : "B",
    "12" : "C",
    "13" : "D",
    "14" : "E",
    "15" : "F",
    "0" : "0"
}

# Form separate lists of keys and values from the hex_list dictionary for cleaner lookup
hex_key_list = list(hex_list.keys())
hex_value_list = list(hex_list.values())

# Binary to Decimal conversion
def bin2dec(binary_number):

    while (True): # Begin input validation

        if not ("1" or "0") in binary_number:
            print("ERROR: Please enter a binary number!")        
        else:   
            conversion = 0
            i = 0

            while i < len(binary_number): # Iterate through each char of the inputted number
                conversion += int(binary_number[len(binary_number)-i-1]) * 2 ** i # And multiply by 2 to the power of i
                i += 1
            
            print(conversion)
            break # Break out of input validation

# Decimal to Binary Conversion
# TODO: Add input validation
def dec2bin(decimal_number):
        
    conversion = ""
    decimal_number = int(decimal_number)

    while decimal_number != 0:
        conversion = str(decimal_number % 2) + conversion # Store remainder of 1 or 0 to the binary string in reverse order
        decimal_number = int(decimal_number / 2) # Make decimal_number equal to itself divided by 2

    print(conversion)

# Hexadecimal to Decimal Conversion
def hex2dec(hex_number):
    
    conversion = 0
    i = 0

    while i < len(hex_number):
        hex_string_indexed = len(hex_number)-i-1 # Create a number to use as an index for easier reference

        if any(j in hex_number[hex_string_indexed] for j in ("A", "B", "C", "D", "E", "F")): # Check if A-F is equal to the currently indexed character
            conversion += int(hex_key_list[hex_value_list.index(hex_number[len(hex_number)-i-1])]) * 16 ** i # Multiply the value by 16 to the power of i
        else:
            conversion += int(hex_number[len(hex_number)-i-1]) * 16 ** i

        i += 1
    
    print(conversion)
        
# Decimal to Hexadecimal Conversion
def dec2hex(decimal_number):

    conversion = ""
    decimal_number = int(decimal_number)

    while decimal_number != 0:
        conversion = hex_list[str(decimal_number % 16)] + conversion # Add to conversion: the remainder of the decimal number divided by 16
        decimal_number = int(decimal_number/16) # Set the decimal number equal to itself divided by 16

    print(conversion)

def bin2hex(binary_number):
    
    while (True):

        if not ("1" or "0") in binary_number:
            print("ERROR: Please enter a binary number!")        
        else:   
            to_hex_conversion = 0
            i = 0

            while i < len(binary_number):
                to_hex_conversion += int(binary_number[len(binary_number)-i-1]) * 2 ** i
                i += 1

            conversion = ""
            
            while to_hex_conversion != 0:
                conversion = hex_list[str(to_hex_conversion % 16)] + conversion
                to_hex_conversion = int(to_hex_conversion/16)

        print(conversion)
        break
        

def hex2bin(hex_number):
    conversion = 0
    i = 0

    while i < len(hex_number):
        hex_string_indexed = len(hex_number)-i-1

        if any(j in hex_number[hex_string_indexed] for j in ("A", "B", "C", "D", "E", "F")):
            conversion += int(hex_key_list[hex_value_list.index(hex_number[len(hex_number)-i-1])]) * 16 ** i
        else:
            conversion += int(hex_number[len(hex_number)-i-1]) * 16 ** i

        i += 1

    to_bin_conversion = ""

    while conversion != 0:
        to_bin_conversion = str(conversion % 2) + to_bin_conversion
        conversion = int(conversion / 2)

    print(to_bin_conversion)
    

        
bin2dec_parser = argparse.ArgumentParser(description="Convert numbers to and from decimal, binary, or hexadecimal")

bin2dec_parser.add_argument("Conversion", metavar="conversion_type", type=str, help="Select conversion type")
bin2dec_parser.add_argument("Number", metavar="number", type=str, help="Input value to be converted")

args = bin2dec_parser.parse_args()

conversion_type = args.Conversion
number = args.Number

if any(i in conversion_type for i in ("b2d", "d2b", "h2d", "d2h", "b2h", "h2b")):
    if conversion_type == "b2d":
        bin2dec(number)
    if conversion_type == "d2b":
        dec2bin(number)
    if conversion_type == "h2d":
        hex2dec(number)
    if conversion_type == "d2h":
        dec2hex(number)
    if conversion_type == "b2h":
        bin2hex(number)
    if conversion_type == "h2b":
        hex2bin(number)
else:
    print("ERROR: Invalid conversion type")
    sys.exit()
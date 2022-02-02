#! /usr/bin/python3

hex_values = {
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

reverse_hex_values = {
    "1" : "1",
    "2" : "2",
    "3" : "3",
    "4" : "4",
    "5" : "5",
    "6" : "6",
    "7" : "7",
    "8" : "8",
    "9" : "9",
    "A": "10",
    "B" : "11",
    "C" : "12",
    "D" : "13",
    "E" : "14",
    "F" : "15",
    "0" : "0"
}

def bin2dec():

    while (True):
        binary_number = input("Please enter a binary number:\n")
        
        if not ("1" or "0") in binary_number:
            print("ERROR: Please enter a binary number!")        
        else:   
            conversion = 0
            i = 0

            while i < len(binary_number):
                conversion += int(binary_number[len(binary_number)-i-1]) * 2 ** i
                # print(len(binary_number)-i-1)
                i += 1
            
            print(conversion)
            break

def dec2bin():
        
    decimal_number = input("Please enter a decimal number:\n")

    conversion = ""
    decimal_number = int(decimal_number)

    while decimal_number != 0:
        conversion = str(decimal_number % 2) + conversion
        decimal_number = int(decimal_number / 2)

    print(conversion)


def hex2dec():
    
    hex_number = input("Please enter a hexadecimal number:\n")
    conversion = 0
    i = 0

    while i < len(hex_number):
        hex_string_indexed = len(hex_number)-i-1

        if any(j in hex_number[hex_string_indexed] for j in ("A", "B", "C", "D", "E", "F")):
            conversion += int(reverse_hex_values[hex_number[len(hex_number)-i-1]]) * 16 ** i
            # print("Letter detected", hex_number[len(hex_number)-i-1])
        else:
            # print("Number detected", hex_number[len(hex_number)-i-1])
            conversion += int(hex_number[len(hex_number)-i-1]) * 16 ** i

        i += 1
    
    print(conversion)
        

def dec2hex():

    decimal_number = input("Please enter a decimal number:\n")

    conversion = ""
    decimal_number = int(decimal_number)

    while decimal_number != 0:

        conversion = hex_values[str(decimal_number % 16)] + conversion
        decimal_number = int(decimal_number/16)

    print(conversion)


hex2dec()
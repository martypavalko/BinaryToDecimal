# Take input as 1's and 0's only
# Iterate through each digit starting from the right-most digit
# Multiply that indexed digit by 2 to the power of the index
# Add all of the products of multipication together for the conversion

def bin2dec():

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
    return conversion

bin2dec()
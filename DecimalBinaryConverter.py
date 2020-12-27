#   Program DecimalBinaryConverter
#
#   Copyright 2020 Ertugrul Harman
#
#       E-mail  : harmancode@gmail.com
#       Twitter : https://twitter.com/harmancode
#       Web     : https://harman.page
#
#   This file is part of DecimalBinaryConverter.
#
#   Flashcards is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with this program.  If not, see <https://www.gnu.org/licenses/>.

# Program DecimalBinaryConverter
# Description:
#   Converts binary numbers to decimal numbers, and vice versa
# Author: Ertugrul Harman
# Date: 8 October 2020
# Revised:
#   <revision date>

# list libraries used

# Declare constants (name in ALL_CAPS)

# Declare Variable types (EVERY variable used)
stay_in_loop = bool()
key = str()
binary = str()
decimal = int()
temp_decimal = int()

stay_in_loop = True

while stay_in_loop:
    key = input("'b' for binary, 'd' for decimal conversion, anything else quits: ").lower()

    if (key != "b") and (key != "d"):
        # User has made an invalid selection. End the program.
        print("Good bye!")
        stay_in_loop = False
        
    else:
        
        if key == "b":
            
            binary = input("Please enter a binary number: ")
            decimal = 0
            
            # Take the length of the binary number, create a range with it from 0 to length - 1
            # and iterate over this range. Example: If binary is 1000, range will be (0, 1, 2, 3).
            for place in range(len(binary)):
                
                # Take the value in the current place and add its place value to the decimal variable.
                # If the value in the current place is zero then there is nothing to add.
                if int(binary[place]) == 1:
                    
                    # Exponent of 2 is length of the binary minus current place minus one.
                    # Example: If current place is 3 and length is 4, exponent is: 4 - 3 - 1 = 0
                    decimal += 2 ** (len(binary) - place - 1)
                    
                elif int(binary[place]) == 0:
                    pass
                    
                else:
                    print ( "error: non-binary bits" )
                
                # end if
                
            # end for
            
            # Conversion is complete. Report the result.
            print(binary, "as decimal equals to", decimal, "\n")
            
        elif key == "d":
            
            decimal = int(input("Please enter a decimal number: "))
            temp_decimal = decimal
            binary = ""
            
            # temp_decimal value will decrease in the while loop because of divisions.
            # Stop the loop if temp_decimal value goes below 1.
            while temp_decimal > 0:
                
                if temp_decimal % 2 == 0:
                    # If remainder of division by 2 is zero, add zero to the binary number.
                    binary = "0" + binary
                    
                else:
                    # If remainder of division by 2 is one, add one to the binary number.
                    binary = "1" + binary
                    
                # end if
                
                # Divide temp_decimal by 2 and keep calculating the remainders in the loop.
                temp_decimal = temp_decimal // 2
                
            # end while
            
            # Conversion is complete. Report the result.
            print(decimal, "as binary equals to", binary, "\n")
            
        else:
            
            print("Oh no!")
            
        # end if (key == "b")
    # end if (key != "b") and (key != "d")
# end while stay_in_loop


# End Program

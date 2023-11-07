# Numerals dictionary
numerals = {1: "I", 4: "IV", 5: "V", 9: "IX", 10: "X", 40: "XL", 50: "L",
            90: "XC", 100: "C", 400: "CD", 500: "D", 900: "CM", 1000: "M"}

# Have a variable to store the number
number = int(input("Enter the integer to convert to a roman numeral: "))

# Created numeral
numeral = ""

for integer in sorted(numerals.keys(), reverse=True):
    # Find the integer division of that number
    multiples = number // integer

    # If division is 0, continue with the rest
    if multiples == 0:
        continue

    # Find the remainder of that number and update number
    number %= integer

    # Create a string concatenation of the numeral
    partial_numeral = multiples * numerals.get(integer)

    # Add the partial numeral to the numeral variable
    numeral += partial_numeral

    # End loop if number is 0
    if number == 0:
        break

print(numeral)

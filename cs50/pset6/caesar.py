import cs50
import sys

# get the cipher key from command line, check for correct num args, and convert to int
if len(sys.argv) != 2:
    print("Please enter your cipher key")

key = int(sys.argv[1])

print("plaintext:")
plaintext = cs50.get_string()
print("ciphertext:")
for i in range(len(plaintext)):
    # Check to make sure we have an alphabetic character
    if plaintext[i].isalpha() == True:
        # Determine whether the character is upper or lowercase
        if plaintext[i].isupper() == True:
            upperLetter = chr(((((ord(plaintext[i]))-65)+key)%26)+65)
            print(upperLetter, end="")
        elif plaintext[i].islower() == True:
            lowerLetter = chr(((((ord(plaintext[i]))-97)+key)%26)+97)
            print(lowerLetter, end="")
    # If the character is a digit, print the ASCII representation
    elif plaintext[i].isdigit() == True:
        print(plaintext[i], end="")
    # If we have any other character, print a space
    else:
        print(" ", end="")
# Print a new line
print()


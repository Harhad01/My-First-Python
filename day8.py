# def geet():
#     print("Hello")
#     print("Welcome out here")
#     print("Have a great day!")

# geet()


# def  greet_with_name(name):
#     print(f"Hello {name}")
#     print(f"Welcome {name}")
    
    
# greet_with_name("Harshad")


# import math
# def paint_calc(height, width, cover):
#     area=height*width
#     nums_of_cans=math.ceil(area/cover)
#     print(f"You'll need {nums_of_cans} cans of paint.")
    
# test_h=int(input("Enter the height: "))
# test_w=int(input("Enter the weight: "))
# coverage=5
# paint_calc(height=test_h, width=test_w, cover=coverage)




# Caesar Cipher Program
# Concepts: Functions, Loops, Conditionals, List Indexing, Modulo Operator

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# FUNCTION DEFINITION (Moved to the top)
def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""
    # Loop through each character in the input text
    for char in start_text:
        # Check if character is in the alphabet (to ignore spaces/symbols)
        if char in alphabet:
            # Find its position in the alphabet list
            position = alphabet.index(char)
            # Calculate new position. Use modulo 26 to wrap around (z -> a)
            new_position = (position + shift_amount) % 26
            # Add the new letter to the result
            end_text += alphabet[new_position]
        else:
            # If it's not a letter (space/symbol), keep it as-is
            end_text += char
    # Print the result using an f-string
    print(f"The {cipher_direction}d text is: {end_text}")

# MAIN PROGRAM LOGIC
should_continue = True

while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    
    # If decoding, make shift negative. Modulo 26 handles large numbers.
    if direction == "decode":
        shift *= -1
    shift = shift % 26  # Ensure shift is within 0-25
    
    # Call the function with user inputs
    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
    
    # Ask user if they want to continue
    result = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if result == "no":
        should_continue = False
        print("Goodbye!")
def cipher(text):
    """Converts text into its numeric representation."""
    result = []
    for letter in text.lower():
        if letter.isalpha():
            # Convert letter to its position number in the alphabet (1 = 'a', 2 = 'b', etc.)
            number = ord(letter) - 96
            # Use parentheses for numbers 10 and above
            if number > 9:
                result.append(f"({number})")
            else:
                result.append(str(number))
        elif letter == " ":
            result.append(" ")
    return " ".join(result)


def decipher(code):
    """Converts numeric code into the corresponding text message."""
    result = []
    # Replace any spaces, split numbers, and remove parentheses
    code = code.replace("(", "").replace(")", "").split()
    for number in code:
        if number.isdigit():
            # Convert number to the corresponding letter
            letter = chr(int(number) + 96)
            result.append(letter)
        elif number == "":
            result.append(" ")
    return "".join(result)


def main():
    # Ask user whether they want to cipher or decipher
    choice = input("Do you want to 'cipher' or 'decipher' the message? ").strip().lower()

    if choice == "cipher":
        text = input("Enter the text to cipher: ")
        result = cipher(text)
        print("Ciphered text:", result)
    elif choice == "decipher":
        code = input("Enter the code to decipher: ")
        result = decipher(code)
        print("Deciphered message:", result)
    else:
        print("Invalid choice. Please type 'cipher' or 'decipher'.")


# Run the program
main()

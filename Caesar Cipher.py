def caesar_cipher(text, shift):
    encrypted_text = ""

    for char in text:
        # Check if the character is an uppercase letter
        if char.isupper():
            # Shift within the range of uppercase letters
            encrypted_text += chr((ord(char) + shift - 65) % 26 + 65)
        # Check if the character is a lowercase letter
        elif char.islower():
            # Shift within the range of lowercase letters
            encrypted_text += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            # Non-alphabetic characters are added unchanged
            encrypted_text += char

    return encrypted_text

def caesar_decrypt(text, shift):
    return caesar_cipher(text, -shift)

def main():
    print("Caesar Cipher Program")

    while True:
        choice = input("Would you like to (E)ncrypt or (D)ecrypt a message? (E/D): ").upper()

        if choice not in ['E', 'D']:
            print("Invalid choice. Please enter 'E' for encrypt or 'D' for decrypt.")
            continue

        message = input("Enter your message: ")
        shift = int(input("Enter the shift value (0-25): "))

        if choice == 'E':
            encrypted_message = caesar_cipher(message, shift)
            print(f"Encrypted Message: {encrypted_message}")
        else:
            decrypted_message = caesar_decrypt(message, shift)
            print(f"Decrypted Message: {decrypted_message}")

        another = input("Would you like to process another message? (Y/N): ").upper()
        if another != 'Y':
          print("Thank you")

          break

if __name__ == "__main__":
    main()
import random
import string

def generate_password(length=12):
    # Characters: letters, digits, and special symbols
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Generate password by randomly picking from characters
    password = ''.join(random.choice(characters) for _ in range(length))
    return password


# Example usage
length = int(input("Enter password length: "))
print("Generated Password:", generate_password(length))

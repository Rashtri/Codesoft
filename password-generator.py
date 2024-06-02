import random
import string

def generate_password(length):
    if length < 4:
        print("Password length should be at least 4 characters.")
        return None

 
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    special = string.punctuation

    all_chars = lower + upper + digits + special
    password = [
        random.choice(lower),
        random.choice(upper),
        random.choice(digits),
        random.choice(special)
    ]

      password += random.choices(all_chars, k=length - 4)

   
    random.shuffle(password)

    
    return ''.join(password)

def main():
    while True:
        try:
            length = int(input("Enter the desired length for the password (or 'q' to quit): "))
            if length == 'q':
                break
            password = generate_password(length)
            if password:
                print(f"Generated password: {password}")
        except ValueError:
            print("Invalid input! Please enter a numeric value or 'q' to quit.")

if __name__ == "__main__":
    main()

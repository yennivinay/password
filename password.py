import random
import string
num_passwords = int(input("How many passwords would you like to generate? "))
def generate_password(length=12):
    while True:
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for _ in range(length))
        # print(password)
        if (any(c.islower() for c in password) and any(c.isupper() for c in password) and any(c.isdigit() for c in password) and len(password) > 7):
            return password

def main():
    password_length = int(input("Enter the length of each password (must be greater than 7): "))
    
    if password_length <= 7:
        print("Password length must be greater than 7.")
        main()
    
    passwords = set()
    
    while len(passwords) < num_passwords:
        password = generate_password(password_length)
        passwords.add(password)
    
    print("\nGenerated Passwords:")
    for password in passwords:
        print(password)

if __name__ == "__main__":
    main()

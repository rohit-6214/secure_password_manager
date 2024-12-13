import secrets
import sys
import os
import json
from cryptography.fernet import Fernet


# Generate or load encryption key
def load_key():
    if not os.path.exists("secret.key"):
        key = Fernet.generate_key()
        with open("secret.key", "wb") as key_file:
            key_file.write(key)
    else:
        with open("secret.key", "rb") as key_file:
            key = key_file.read()
    return Fernet(key)

# Generate a password
def generate_password(length, strength):
    lower = 'abcdefghijklmnopqrstuvwxyz'
    upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    digits = '0123456789'
    symbols = '!@#$%^&*()-_=+[]{}|;:,.<>?'
    
    if strength == 'weak':
        all_characters = lower
    elif strength == 'medium':
        all_characters = lower + upper
    elif strength == 'strong':
        all_characters = lower + upper + digits + symbols
    else:
        raise ValueError("Invalid strength choice! Choose 'weak', 'medium', or 'strong'.")
    
    password = []
    if strength == 'medium':
        password.append(secrets.choice(lower))
        password.append(secrets.choice(upper))
    elif strength == 'strong':
        password.append(secrets.choice(lower))
        password.append(secrets.choice(upper))
        password.append(secrets.choice(digits))
        password.append(secrets.choice(symbols))
    
    password += [secrets.choice(all_characters) for _ in range(length - len(password))]
    return ''.join(password)

# Save password to a JSON file, storing entries in an array format
def save_password(service, username, password, fernet):
    encrypted_password = fernet.encrypt(password.encode()).decode()
    new_entry = {
        "service": service,
        "username": username,
        "encrypted_password": encrypted_password
    }
    
    # Load existing passwords
    if os.path.exists("passwords.json"):
        with open("passwords.json", "r") as file:
            try:
                password_list = json.load(file)
            except json.JSONDecodeError:
                password_list = []
    else:
        password_list = []
    
    # Append new entry to the list
    password_list.append(new_entry)
    
    # Save the updated list to the JSON file
    with open("passwords.json", "w") as file:
        json.dump(password_list, file, indent=2)
    
    print(f"Password for {service} saved successfully!")

# Retrieve password for a service from the JSON file
def retrieve_password(service, username, fernet):
    if not os.path.exists("passwords.json"):
        print("No passwords saved yet.")
        return

    with open("passwords.json", "r") as file:
        password_list = json.load(file)
    
    for entry in password_list:
        if entry["service"] == service and entry["username"] == username:
            decrypted_password = fernet.decrypt(entry["encrypted_password"].encode()).decode()
            print(f"Service: {entry['service']}")
            print(f"Username: {entry['username']}")
            print(f"Password: {decrypted_password}")
            return
    
    print(f"No password found for service '{service}' and username '{username}'.")

# Update password for a service if it exists
def update_password(service, username, new_password, fernet):
    if not os.path.exists("passwords.json"):
        print("No passwords saved yet.")
        return
    
    updated = False

    with open("passwords.json", "r") as file:
        password_list = json.load(file)
    
    # Update password if service + username match is found
    for entry in password_list:
        if entry["service"] == service and entry["username"] == username:
            entry["encrypted_password"] = fernet.encrypt(new_password.encode()).decode()
            updated = True
            print(f"Password updated for {service} and username {username}.")
            break
    
    if updated:
        # Save the updated list back to the file
        with open("passwords.json", "w") as file:
            json.dump(password_list, file, indent=2)
    else:
        print(f"No password found for service '{service}' and username '{username}'.")

# Main function
def main():
    fernet = load_key()

    while True:
        print("\nPassword Manager Menu:")
        print("1. Generate Password")
        print("2. Store Password")
        print("3. Retrieve Password")
        print("4. Update Password")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            length = int(input("Enter the desired password length: "))
            if length < 4:
                print("Password must be at least 4 characters long.")
                sys.exit()
            strength = input("Choose password strength (weak, medium, strong): ").lower()
            generated_password = generate_password(length, strength)
            print(f"Generated Password: {generated_password}")

        elif choice == "2":
            service = input(" Please Enter your name: ")
            username = input("Enter your username: ")
            password = input("Enter your password (or press Enter to generate one): ")
            if not password:
                length = int(input("Enter the desired password length: "))
                if length < 4:
                    print("Password must be at least 4 characters long.")
                    sys.exit()
                strength = input("Choose password strength (weak, medium, strong): ").lower()
                password = generate_password(length, strength)
                print(f"Generated Password: {password}")
            save_password(service, username, password, fernet)

        elif choice == "3":
            service = input("Please Enter your name: ")
            username = input("Enter your username: ")
            retrieve_password(service, username, fernet)

        elif choice == "4":
            service = input("Enter the service name to update: ")
            username = input("Enter your username: ")
            new_password = input("Enter your new password (or press Enter to generate one): ")
            if not new_password:
                length = int(input("Enter the desired password length: "))
                if length < 4:
                    print("Password must be at least 4 characters long.")
                    sys.exit()
                strength = input("Choose password strength (weak, medium, strong): ").lower()
                new_password = generate_password(length, strength)
                print(f"Generated Password: {new_password}")
            update_password(service, username, new_password, fernet)

        elif choice == "5":
            print("Exiting password manager.")
            sys.exit()

        else:
            print("Invalid option. Please choose a valid option.")

if __name__ == "__main__":
    main()

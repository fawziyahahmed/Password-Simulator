import random
import string

# Function to generate a random password
def generate_password(length=12):
    # Define acceptable characters for the password
    acceptable_chars = string.ascii_letters + string.digits + string.punctuation
    
    # Generate a password with the specified length using acceptable characters
    password = ''.join(random.choice(acceptable_chars) for _ in range(length))
    return password

# Function to check if the password is acceptable
def is_acceptable(password):
    # Check if the password contains special symbols
    has_special_symbol = any(char in string.punctuation for char in password)
    
    # Check if the password is not a word in a dictionary list (example here)
    dictionary_list = ['password', '123456', 'happy', 'iloveme']
    not_in_dictionary = password not in dictionary_list
    
    return has_special_symbol and not_in_dictionary

# Main function
def main():
    accepted_passwords = []
    iterations = 0
    
    while iterations < 40:
        password = generate_password()
        if is_acceptable(password):
            accepted_passwords.append(password)
            iterations += 1
            print(f"Iteration {iterations}: Accepted password - {password}")
        else:
            print(f"Iteration {iterations}: Unaccepted password - {password}")
    
    print("\nAccepted passwords:")
    for idx, accepted_password in enumerate(accepted_passwords, start=1):
        print(f"{idx}. {accepted_password}")

if __name__ == "__main__":
    main()
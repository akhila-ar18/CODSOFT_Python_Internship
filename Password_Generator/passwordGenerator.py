import random
import string

def generate_password(length):
    # This line is used to define the characters to be used in the password
    characters = string.ascii_letters + string.digits + string.punctuation

    # This line generates the password using random.choice to select characters randomly
    password = ''.join(random.choice(characters) for i in range(length))
    return password

def main():
    while True:
        # This line Prompts the user to specify the desired length of the password
        length = int(input("Enter the desired length of the password: "))

        # This line generates the password
        password = generate_password(length)

        # This line displays the generated password
        print("Generated Password:", password)

        choice = input("Do you still wanna continue(1/0)? ")
        print("\n")
        
        if(choice != "1"):
            print("Exiting...")
            break
        else:
            continue

if __name__ == "__main__":
    main()

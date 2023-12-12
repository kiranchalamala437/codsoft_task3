import random
import string
def generate_password(length):

    all_characters = string.ascii_letters + string.digits + string.punctuation
    
    #generating a rondom password
    password = "".join(random.choice(all_characters) for i in range(length))
    return password

password_length = int(input("Enter length of the password: "))

password = generate_password(password_length)

print(f"The generated password is: {password}")
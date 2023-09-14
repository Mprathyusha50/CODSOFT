import random
import string
def generate_password(length):
    #define characters to use in the password
    characters=string.ascii_lowercase+string.digits
    #generate a random password using specified length
    password=''.join(random.choice(characters)for i in range(length))
    return password
#prompt the user for the desired password length
try:
    ch = 1
    while(ch!=0):
        password_length=int(input("enter the desired password length:"))
        if password_length<=0:
            print("please enter a positive length.")
            #generate and display the password generated_password=generate_password(password_length)
        print("Generated PassWord:",generate_password(password_length))
        ch = int(input("Enter a value:"))
except ValueError:
    print("invalid input.please enter a valid positive integer for the password length.")
        
        

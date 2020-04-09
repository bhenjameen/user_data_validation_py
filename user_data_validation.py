import random
import string

first_name=input("Welcome, Enter your First Name:  ") 
last_name=input("Enter your Last Name:   ")
email=input("Enter your E-mail:  ")

def passwordInput():
    length =1
    while length < 7:
        print("Type a password of your choice")
        print("Password must be 7 characters or more:  ")
        password=input()
        length=len(password)
    return password

def randomString(stringlength=5):
    letter = string.ascii_lowercase
    return ''.join(random.choice(letter) for i in range (stringlength))

def queryPassword():
    query = " "
    while query.lower() != 'yes' or query.lower() != 'no':
        query = input("Will you like to continue with this Password or change it? Type 'yes' to continue or 'no' to change it:   ")
        if query.lower() == 'yes' or query.lower() == 'no':
            break
    return query

first_part = first_name[0:2]
second_part = last_name[-2:]
password = first_part + randomString() + second_part
print("Your Password is " + password)


if queryPassword() == "no":
    password=passwordInput()    

user_data=[first_name,last_name,email,password]

print(user_data)
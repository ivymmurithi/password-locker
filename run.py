#!/usr/bin/env python3.10

import random
import string

from account_login import User
from credentials_pass import Credentials

def new_logins(user_name,password):
    """
    create user logins
    """
    logins = User(user_name,password)
    return logins

def new_credentials(social_name,social_username,social_password):
    credentials = Credentials(social_name,social_username,social_password)
    return credentials

def save_user_logins(logins):
    """
    save user logins
    """
    logins.save_user_logins()

def save_credentials(credentials):
    credentials.save_socials()

def delete_logins(logins):
    """
    Function that deletes logins
    """
    logins.delete_user_logins()

def delete_socials(credentials):
    credentials.delete_socials()

def find_username(user_name):
    """
    Authenticates username entered
    """
    return User.username_authentication(user_name)

def find_password(password):
    """
    Authenticates password entered
    """
    return User.password_authentication(password)

def username_exists(user_name):
    """
    check if their is a username object
    """
    return User.username_exists(user_name)

def password_exists(password):
    """
    Check if password object exists
    """
    return User.password_exists(password)

def display_user_logins():
    """
    Display user logs
    """
    return User.display_logins()

def display_credentials():
    return Credentials.display_socials()

def main():
    print("Keep your password safe with password locker \n")

    while True:

        print("Use these to maneuver: \n 1. Create Account \n 2. Sign Up \n")

        option = int(input())

        if option == 1:
            
            print("Create your username")

            user_name = input()

            print("\n 1. Create Password \n 2. Generate Password")
            choices = int(input())

            if choices == 1:

                print("Create your password")

                password = input()

                save_user_logins(new_logins(user_name, password))

                print(f"Hello {user_name}")

            elif choices == 2:
                length = int(input("Enter the length of password \n"))
                lower = string.ascii_lowercase
                upper = string.ascii_uppercase
                num = string.digits
                symbols = string.punctuation
                all = lower + upper + num + symbols
                temp = random.sample(all,length)
                password = "".join(temp)
                print(password)
                print("\n")

            while True:

                print("Choose what you'd like to do \n")

                print("\n 1. Add credentials \n 2. Display credentials \n 3. Delete credentials \n")

                choice = int(input())

                if choice == 1:

                    print("Enter social platform name")

                    social_name = input()

                    print("Enter username")

                    social_username = input()

                    print("Enter password")

                    social_password = input()

                    save_credentials(new_credentials(social_name,social_username,social_password))

                    print("\n")

                elif choice == 2:

                    if display_credentials():
                        for crendential in display_credentials():
                            print(f"Social Name: {crendential.social_name} \n Username: {crendential.social_username} \n Password: {crendential.social_password} \n")
                    else:
                        print("No credentials found")

                elif choice == 3:
                    delete_socials(Credentials)
        
        elif option == 2:

            print("Enter your username")

            user_name =input()

            print("Enter Password")

            password = input()

            print(f"Logged in as {user_name}")

            print("\n")

            while True:

                print("Choose what you'd like to do \n")

                print("\n 1. Add credentials \n 2. Display credentials \n 3. Delete credentials \n")

                choice = int(input())

                if choice == 1:

                    print("Enter social platform name")

                    social_name = input()

                    print("Enter username")

                    social_username = input()

                    print("Enter password")

                    social_password = input()

                    save_credentials(new_credentials(social_name,social_username,social_password))

                    print("\n")

                elif choice == 2:

                    if display_credentials():
                        for crendential in display_credentials():
                            print(f"Social Name: {crendential.social_name}\n Username: {crendential.social_username} \n Password: {crendential.social_password} \n")
                    else:
                        print("No credentials found")


            



if __name__ == "__main__":
    main()


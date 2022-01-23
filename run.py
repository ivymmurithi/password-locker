#!/usr/bin/env python3.10

from account_login import User

def new_logins(user_name,password):
    """
    create user logins
    """
    logins = User(user_name,password)
    return logins

def save_user_logins(logins):
    """
    save user logins
    """
    logins.save_user_logins()

def delete_logins(logins):
    """
    Function that deletes logins
    """
    logins.delete_user_logins()

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

def main():
    print("Keep your password safe with password locker \n")

    while True:

        print("Use these to maneuver: \n 1. Create Account \n 2. Sign Up \n 3. Delete Account \n")

        option = int(input())
    
        if option == 1:
            
            print("Create your username")

            user_name = input()

            print("Create your password")

            password = input()

            save_user_logins(new_logins(user_name,password))

            print(f"Hello {user_name}")

            while True:
                print("1. Add credentials \n 2. Display credentials \n 3. Delete credentials \n")

            




if __name__ == "__main__":
    main()


#!/usr/bin/env python3.10

from account_login import User

def new_logins(user_name,password):
    """
    create an instance of user logins
    """
    new_user = User(user_name,password)
    return new_user

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

def find_username(string):
    """
    Authenticates username entered
    """
    return User.username_authentication(string)

def find_password(string):
    """
    Authenticates password entered
    """
    return User.password_authentication(string)

def username_exists(string):
    """
    check if their is a username object
    """
    return User.username_exists(string)

def password_exists(string):
    """
    Check if password object exists
    """
    return User.password_exists(string)

    

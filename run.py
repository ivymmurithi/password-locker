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

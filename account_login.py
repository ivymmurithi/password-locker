class User:
    """
    A class that generates new instances of user accounts created
    """

    def __init__(self,user_name,password):
        """
        This method will create new instances of the User class.

        Args:
        user_name: New User username.
        password: New password for password.
        """

        self.user_name = user_name
        self.password = password


    user_logins = []
    """
    An empty list to store the user_name and password
    """

    def save_user_logins(self):
        """
        Method for saving the created user accounts
        """

        User.user_logins.append(self)

    def delete_user_logins(self):
        """
        Method for deleting users
        """
        User.user_logins.remove(self)

    @classmethod
    def username_authentication(cls,user_name):
        """
        Method that checks for the inputed username and 
        returns the username
        """

        for user in cls.user_logins:
            if user.user_name == user_name:
                    return user

    @classmethod
    def password_authentication(cls,password):
        """
        Method that checks for the inputed password and 
        returns the user password and account
        """

        for user in cls.user_logins:
            if user.password == password:
                return user

    @classmethod
    def username_exists(cls,user_name):
        """
        Method that checks if the username added username exists inside user_logins list
        """

        for user in cls.user_logins:
            if user.user_name == user_name:
                return True

        return False 

    @classmethod
    def password_exists(cls,password):
        """
        Method that checks if the username added username exists inside user_logins list
        """

        for user in cls.user_logins:
            if user.password == password:
                return True

        return False

    @classmethod
    def display_logins(cls):
        """
        Returns all user logins
        """

        return cls.user_logins




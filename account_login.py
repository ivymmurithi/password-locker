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


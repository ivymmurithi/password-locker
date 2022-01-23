class Credentials:
    """
    Class that generates new instances of credentials
    """

    def __init__(self,social_username,social_password):
        
        self.social_username = social_username
        self.social_password = social_password

        socials_list = []
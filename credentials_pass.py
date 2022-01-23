class Credentials:
    """
    Class that generates new instances of credentials
    """

    def __init__(self,social_username,social_password):
        
        self.social_username = social_username
        self.social_password = social_password

    socials_list = []
    """
    Empty list to store socials username and password
    """

    def save_socials(self):
        Credentials.socials_list.append(self)

    def delete_socials(self):
        Credentials.socials_list.remove(self)

    @classmethod
    def display_socials(cls):
        return cls.socials_list
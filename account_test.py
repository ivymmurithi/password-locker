from cgi import test
import unittest
"""
Importing unittest module
"""

from account_login import User
"""
Importing the User class
"""

class TestUser(unittest.TestCase):
    """
    Shows the User class behaviours during tests
    """

    def setUp(self):
        """
        Creates new User Object
        """ 
        self.new_user = User("Ivy","1234") 

    def tearDown(self):
        User.user_logins = []

    def test_init(self):
        """
        Test if the object is initialized the right way
        """

        self.assertEqual(self.new_user.user_name,"Ivy")
        self.assertEqual(self.new_user.password,"1234")

    def test_save_user_logins(self):
        """
        Test save_user_logins if it's actually saving the new username 
        and password
        """
        self.new_user.save_user_logins()
        self.assertEqual(len(User.user_logins),1)

    def test_save_users(self):
        """
        Test saving many user accounts
        """
        self.new_user.save_user_logins()
        test_user = User("Monga","4321")
        test_user.save_user_logins()
        self.assertEqual(len(User.user_logins),2)

    def test_delete_user_logins(self):
        """
        Test if users are being deleted
        """
        self.new_user.save_user_logins()
        test_user = User("Monga","4321")
        test_user.save_user_logins()
        self.new_user.delete_user_logins()
        self.assertEqual(len(User.user_logins),1)



if __name__ == '__main__':
    unittest.main()

    
    
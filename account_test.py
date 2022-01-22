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

    def test_init(self):
        """
        Test if the object is initialized the right way
        """

        self.assertEqual(self.new_user.user_name,"Ivy")
        self.assertEqual(self.new_user.password,"1234")

if __name__ == '__main__':
    unittest.main()

    
    
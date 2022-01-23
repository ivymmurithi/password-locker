import unittest

from credentials_pass import Credentials

class TestCredentials(unittest.TestCase):

    def setUp(self):

        self.new_credentials = Credentials("FeuerMuschi","12345")

    def test_init(self):
        self.assertEqual(self.new_credentials.social_username,"FeuerMuschi")
        self.assertEqual(self.new_credentials.social_password,"12345")



if __name__ == "__main__":
    unittest.main()
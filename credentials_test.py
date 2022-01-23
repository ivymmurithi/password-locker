import unittest

from credentials_pass import Credentials

class TestCredentials(unittest.TestCase):

    def setUp(self):

        self.new_credentials = Credentials("Instagram","FeuerMuschi","12345")

    def tearDown(self):
        Credentials.socials_list = []

    def test_init(self):
        self.assertEqual(self.new_credentials.social_name,"Instagram")
        self.assertEqual(self.new_credentials.social_username,"FeuerMuschi")
        self.assertEqual(self.new_credentials.social_password,"12345")

    def test_save_socials(self):
        self.new_credentials.save_socials()
        self.assertEqual(len(Credentials.socials_list),1)

    def test_delete_socials(self):
        self.new_credentials.save_socials()
        self.assertEqual(len(Credentials.socials_list),1)

    def test_display_socials(self):
        self.assertEqual(Credentials.display_socials(),Credentials.socials_list)


if __name__ == "__main__":
    unittest.main()
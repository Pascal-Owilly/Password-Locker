
import unittest
from PasswordLocker import User
from PasswordLocker import Credentials

class CredentialTest(unittest.TestCase):
    '''
    Generates new instance of class
    '''

def setUp(self):
    '''
    This is a unit test case that helps in creating test cases
    '''

    self.new_account = User("Test", "abc123")

def test_init(self):
    '''
    test init is a test case thst tests if the object is initialised properly
    '''
    self.assertEqual(self.new_account.username,"Test")
    self.assertEqual(self.new_account.password,"abc123")

def test_save_account(self):

    self.new_account.save_account()
    self.assertEqual(len(User.userAccounts),1)

if __name__ =='__main__':
    unittest.main()        

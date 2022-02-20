import unittest
from PasswordLocker import User

def setUp(self):

    self.new_account = User("Pascal", "abc123")

def test_save_account(self):

    self.new_account.save_account()
    self.assertEqual(len(User.userAccounts),1)

if __name__ =='__main__':
    unittest.main()        

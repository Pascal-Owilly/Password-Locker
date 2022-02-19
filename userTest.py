import unittest
from user import User

class TestUserDetails(unittest.TestCase):
    '''
    Test case tests if the user name password match
    '''
    newUserDetails = [] # add empty array to hold new user details

    def setUp(self):
        '''
        set up method run before each test case
        '''
        self.newUserDetails = User("Pascal","abc123") # User object

    def test__init__(self):
        '''
        Test if the object is initialized properly
        '''  
        self.assertEqual(self.newUserDetails.userName,"Pascal")
        self.assertEqual(self.newUserDetails.password, "abc123")

if __name__== '__main__':
    unittest.main()        
        

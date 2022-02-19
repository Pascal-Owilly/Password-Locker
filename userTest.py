import unittest # Importing the unittest module
from PasswordLocker import User # Importing the contact class

class TestContact(unittest.TestCase):

    '''
    Test class that defines test cases for the contact class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''


    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_contact = User("Pascal", "abc123") # create contact object


    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_contact.userName,"Pascal")
        self.assertEqual(self.new_contact.UserPassword,"abc123")

    def test_save_credential(self):
        '''
        test_save_contact test case to test if the contact object is saved into
         the contact list
        '''
        self.new_contact.save_credential() # saving the new contact
        self.assertEqual(len(User.accounts),1)   

    
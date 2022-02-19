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
        self.assertEqual(self.new_contact.userPassword,"abc123")

    def test_save_credential(self):
        '''
        test_save_contact test case to test if the contact object is saved into
         the contact list
        '''
        self.new_contact.save_credential() # saving the new contact
        self.assertEqual(len(User.accounts),1)   

    def test_save_credentials(self):
            '''
            test_save_multiple_contact to check if we can save multiple contact
            objects to our contact_list
            '''
            self.new_contact.save_credential()
            test_credential = User("Test","user") # new contact
            test_credential.save_credential()
            self.assertEqual(len(User.accounts),2)

    def tearDown(self):
            '''
            tearDown method that does clean up after each test case has run.
            '''
            User.accounts = []

# other test cases here
    def test_save_credentials(self):
            '''
            test_save_multiple_contact to check if we can save multiple contact
            objects to our contact_list
            '''
            self.new_contact.save_credential()
            test_credential = User("Test","user") # new contact
            test_credential.save_credential()
            self.assertEqual(len(User.accounts),2)        
  
    def test_delete_credential(self):
            '''
            test_delete_contact to test if we can remove a contact from our contact list
            '''
            self.new_contact.save_credential()
            test_credential = User("Test","user") # new contact
            test_credential.save_credential()

            self.new_contact.delete_credential()# Deleting a contact object
            self.assertEqual(len(User.accounts),1) 

    def test_find_credential_by_userName(self):
        '''
        test to check if we can find a contact by userName and display information
        '''

        self.new_contact.save_credential()
        test_credental = User("Test","abc123") # new contact
        test_credental.save_credential()

        found_credential = User.find_by_userName("Pascal")

        self.assertEqual(found_credential.userPassword,test_credental.userPassword)
    

if __name__ == '__main__':
    unittest.main()
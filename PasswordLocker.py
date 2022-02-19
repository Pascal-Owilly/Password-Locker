class User:
    """
   This class  generates new instances of user accounts.
    """

    accounts = [] # Empty 

    def __init__(self,userName,userPassword):

      # docstring removed for simplicity

        self.userName = userName
        self.userPassword = userPassword
        

    def save_credential(self):

        '''
        save_contact method saves contact objects into contact_list
        '''

        User.accounts.append(self)

    def delete_credential(self):

        '''
        delete_contact method deletes a saved contact from the contact_list
        '''

        User.accounts.remove(self)


    @classmethod
    def find_by_userName(cls,userName):
        '''
        Method that takes in a userName and returns a contact that matches that name.

        Args:
            number: Phone number to search for
        Returns :
            Contact of person that matches the number.
        '''

        for credential in cls.accounts:
            if credential.userName == userName:
                return credential    
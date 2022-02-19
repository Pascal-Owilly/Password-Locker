class User:
    """
   This class  generates new instances of user accounts.
    """

    accounts = [] # Empty 

    def __init__(self,userName,userPassword):

      # docstring removed for simplicity

        self.userName = userName
        self.UserPassword = userPassword
        

    def save_credential(self):

        '''
        save_contact method saves contact objects into contact_list
        '''

        User.accounts.append(self)
class User:
    '''
    The User class generates a new instance of the class
    '''
    userAccounts = [] # create empty accounts list to save all the user accunts

    def __init__(self,username,password):
        self.username = username
        self.pasword = password

    def save_account(self):
        User.userAccounts.append(self)

    def show_accounts(cls):
        return cls.userAccounts   

    @classmethod
    def show_accounts(cls):
        '''
        method that returns the accounts list
        '''
        return cls.userAccounts
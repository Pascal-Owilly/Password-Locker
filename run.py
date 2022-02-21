#!/usr/bin/env python3.9
from PasswordLocker import User
from credential import Credentials
import random
import string

def create_account(username,password):
    '''
    Function to create a new account
    '''
    new_account = User(username,password)
    return new_account

def save_account(account):
    '''
    Function to save account
    '''
    account.save_account()  

def del_account(account):
    '''
    Function to delete an account
    '''
    account.delete_account()

def find_account(username):
    '''
    Function that finds a contact by username and returns the account
    '''
    return User.find_by_username(username)   

def check_existing_accounts(username):
    '''
    Function that check if an account exists with that username and return a Boolean
    '''
    return User.account_exist(username)   

def show_user():
        '''
        function that returns users details
        ''' 
        return Credentials.f_name + Credentials.l_name  
        

def show_accounts():
    '''
    Function that returns all the saved accounts
    '''
    return User.show_accounts() 


# generate a random password
def get_random_string(length):
    randon_uppercase_letter = string.ascii_uppercase
    result_str = ''.join(random.choice(randon_uppercase_letter) for i in range(length))
 

    print("*"*30)
    print("WELCOME TO YOUR ACCOUNT CREATION")
    print("*"*30)
    print("You can use your generated password below or create a new one")
    print("\n")
    
    print(result_str)
    print("\n") 
    print("_"*60)
get_random_string(7)
  

def main():
        while True:
                print("Use the following short codes to naviagate to your account:")
                print("*"*20)
                print("ac: new user account")
                print("*"*20)
                print("lgn: login to your existing accout") 
                print("*"*20)
                print("va: view all accounts")
                print("*"*20)
                print("exit: to exit accout")
                print("*"*20)
                shortCode = input().lower()
                print("\n")

                if shortCode == "ac":
                        print("Create new account")
                        print("\n")
                        print("Input your username")
                        u_name = input()
                        print("\n")
                        print("Create your password")
                        pwd = input()
                        print("confirm password")
                        pwd_confirm = input()
                        
                        while pwd != pwd_confirm:
                                print("Invalid password, ensure passwords match")
                                print("Create your password")  
                                pwd = input()
                                print("Confirm password")
                                pwd_confirm = input()
                                print("\n")

                        else:
                                print("\n")
                                print("_"*60)
                                print("_"*60)
                              
                                print("You have successfully created your account ")
                                print("\n")
                                print("_"*60)
                                print("_"*60)
                                print("_"*60)
                                print("Login to your account")
                                print("\n")
                                print("Input username")
                                login_u_name = input()
                                print("Enter your password")
                                login_pwd = input()
                                print("_"*60)
                                print("_"*60)
                                print("_"*60)
                        while u_name != login_u_name or login_pwd != pwd:
                                print("Invalid credentials, try again")
                                print("Enter your username")
                                login_u_name = input()
                                print("Enter Password")
                                login_pwd = input()
                                print("\n")
                                print("_"*60)
                                print("_"*60)
                                print("_"*60)

                        else:
                                print("Hello, welcome aboard")
                                print("_"*60)
                                print("_"*60)
                                print("_"*60)

                elif shortCode == "":
                        print("Empty request, input short code")  
                
                elif shortCode == 'va':

                            if show_accounts():
                                    print("Here is a list of all your accounts")
                                    print('\n')

                                    for account in show_accounts():
                                            print(f"{account.username} {account.password}")

                                    print('\n')
                            else:
                                    print('\n')
                                    print("You dont have any accounts saved yet")
                                    print('\n')
                                    print("_"*60)
                                    print("_"*60)
                                    print("_"*60)
                elif shortCode == "lgn":
                        print("To login to your account, input your credentials below:") 
                        print("Enter your username")
                        login_u_name = input()
                        print("Enter Password")
                        login_pwd = input()
                        print("\n")    
                        print("Login successful")               
               
                elif shortCode == "exit":
                        print("Exiting program..........")
                        break         

if __name__== '__main__':
        main()                            




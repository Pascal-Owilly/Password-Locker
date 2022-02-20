#!/usr/bin/env python3.9
from PasswordLocker import User
import random
import string

def create_contact(username,password):
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


def show_accounts():
    '''
    Function that returns all the saved accounts
    '''
    return User.show_accounts() 


# generate a random password
def get_random_string(length):
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    print("You can use your generated password below or create a new one")
    print("\n")
    print(result_str)
    print("\n")
get_random_string(5)
    
    




def main():
        while True:
                print("Welcome to your account creation")
                print("\n")
                print("Use the following short codes to naviagate to your account:")
                print("ac: new user account")
                print("lgn: login to your existing accout") 
                print("da: dispaly all accounts")
                print("exit: to exit accout")
                print("\n")
                shortCode = input().lower()

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
                                print("You have successfully created your account ")
                                print("\n")
                                print("Login to your account")
                                print("\n")
                                print("Input username")
                                login_u_name = input()
                                print("Enter your password")
                                login_pwd = input()

                        while u_name != login_u_name or login_pwd != pwd:
                                print("Invalid credentials, try again")
                                print("Enter your username")
                                login_u_name = input()
                                print("Enter Password")
                                login_pwd = input()
                                print("\n")

                        else:
                                print("Hello, welcome aboard")

                elif shortCode == "":
                        print("Empty request, input short code")  
                
                elif shortCode == 'da':

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




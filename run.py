#!/usr/bin/env python3.9
import unittest
from PasswordLocker import User

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

 


def main():
        while True:
                print("Welcome to your account creation")
                print("\n")
                print("Use the following short codes to naviagate to your account:")
                print("ac: new user account, lgn: login to your existing accout, sv: save account account, exit: to exit accout, da: dispaly all accounts")
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
                                print("You have successfully created your account ")
                                print("Login to your account")
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
                                    print("You dont seem to have any contacts saved yet")
                                    print('\n')
               
                elif shortCode == "exit":
                        break         

if __name__== '__main__':
        main()                            




import unittest
from PasswordLocker import User

def main():
        while True:
                print("Welcome to your account creation")
                print("\n")
                print("Use the following short codes to naviagate to your account:")
                print("ac: new user account, lgn: login to your existing accout, adc: add new account, exit: to exit accout")
                print("\n")
                shortCode = input().lower()

                if shortCode == "ac":
                        print("Create new account")
                        print("\n")
                        print("Input your username")
                        u_name = input().capitalize
                        print("\n")
                        print("Create your password")
                        pwd = input()
                        print("confirm password")
                        pwd_confirm = input()
                        
                



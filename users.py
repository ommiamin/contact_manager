import re
import pickle
import os.path

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def create_account():
        # Function to add a new contact
        username = input("Enter username: ")
        password = input("Enter password with 8 character: ")
        while not re.match(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[!@#$%^&*])(?=.{8,})", password):
            password = input("your password is weak: ")
        password2 = input("Please re-enter your password : ")
        while not (password == password2):
            password2 = input("Invalid phone number. Please re-enter your password : ")
            
        contacts2.append(User(username, password))
        print("Contact added successfully!") 

    def authenticate():
        username = input("Enter username: ")
        
        for contact in contacts2 :
            while not(contact.username == username) :
                username = input("Username is not correct , Enter username: ")
            password = input("Enter password : ")
            while not(contact.password == password ):
                password = input("Password is not correct , Enter password : ")    
            print("welcome")
            return True
            

    def change_password():
        # Function to edit an existing contact
        username = input("Enter the username of the user to edit: ")
        for contact in contacts2:
            if contact.username == username:
                password = input("Enter the new password of the user: ")
                while not re.match(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[!@#$%^&*])(?=.{8,})", password):
                    password = input("your password is weak: ")
                password2 = input("Please re-enter your password : ")
                while not (password == password2):
                    password2 = input("Invalid phone number. Please re-enter your password : ")
                contact.password = password
                print("Contact updated successfully!")
                return
        print("user not found.")



filename1 = "/home/ommiamin/teamproject/m98-hw9/contact_manager/data/users.pickle"

if os.path.isfile(filename1) and os.path.getsize(filename1) > 0:
    with open(filename1, "rb+") as f:
        try:
            contacts2 = pickle.load(f)
        except EOFError:
            contacts2 = []
else:
    contacts2 = []
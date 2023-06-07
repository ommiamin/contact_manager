import re
import os.path
import pickle

class Contact:
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone

    def add_contact():
        # Function to add a new contact
        name = input("Enter the name of the contact: ")
        email = input("Enter the email of the contact: ")
        while not re.match(r"([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+", email):
            email = input("Invalid email address. Enter a valid email address: ")
        phone = input("Enter the phone number of the contact: ")
        while not re.match(r"^09(1[0-9]|3[1-9])-?[0-9]{3}-?[0-9]{4}$", phone):
            phone = input("Invalid phone number. Enter a 10-digit phone number: ")
        contacts1.append(Contact(name, email, phone))
        print("Contact added successfully!")
            

    def edit_contact():
        # Function to edit an existing contact
        name = input("Enter the name of the contact to edit: ")
        for contact in contacts1:
            if contact.name.lower() == name.lower():
                email = input("Enter the new email of the contact: ")
                while not re.match(r"([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+", email):
                    email = input("Invalid email address. Enter a valid email address: ")
                phone = input("Enter the new phone number of the contact: ")
                while not re.match(r"^09(1[0-9]|3[1-9])-?[0-9]{3}-?[0-9]{4}$", phone):
                    phone = input("Invalid phone number. Enter a 10-digit phone number: ")
                contact.email = email
                contact.phone = phone
                print("Contact updated successfully!")
                return
        print("Contact not found.")

    def delete_contact():
        # Function to delete a contact
        name = input("Enter the name of the contact to delete: ")
        for contact in contacts1:
            if contact.name.lower() == name.lower():
                contacts1.remove(contact)
                print("Contact deleted successfully!")
                return
        print("Contact not found.")
    
    # Function to view all contacts
    def view_contacts():
        for contact in contacts1:
            print("-" *20)
            print(f"{contacts1.index(contact)+1}) Name: {contact.name}-Email: {contact.email}-Phone: {contact.phone}")
            print("-" *20)


filename = "/home/ommiamin/teamproject/m98-hw9/contact_manager/data/contacts.pickle"

if os.path.isfile(filename) and os.path.getsize(filename) > 0:
    with open(filename, "rb+") as f:
        try:
            contacts1 = pickle.load(f)
        except EOFError:
            contacts1 = []
else:
    contacts1 = []

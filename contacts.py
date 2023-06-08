import re
import os.path
import pickle

class Contact:
    def __init__(self, name, email, phone , note  ):
        self.name = name
        self.email = email
        self.phone = phone
        self.note = note

    def add_contact():
        # Function to add a new contact
        name = input("Enter the name of the contact: ")
        email = input("Enter the email of the contact: ")
        while not re.match(r"([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+", email):
            email = input("Invalid email address. Enter a valid email address: ")
        phone = input("Enter the phone number of the contact: ")
        while not re.match(r"^09(1[0-9]|3[0-9])-?[0-9]{3}-?[0-9]{4}$", phone):
            phone = input("Invalid phone number. Enter a 11-digit phone number: ")
        contacts1.append(Contact(name, email, phone ,note=""))
        
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
                while not re.match(r"^09(1[0-9]|3[0-9])-?[0-9]{3}-?[0-9]{4}$", phone):
                    phone = input("Invalid phone number. Enter a 11-digit phone number: ")
                noteok=input("do you want add note for contatc ?(Y/n)")
                if (noteok == "y" , noteok == "Y"):
                    note = input("Enter your note for this contact: ")
                    contact.note = note
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
    
    def search_contact():
        search_name =input ("What do you want to search for?(type : name , email , phone)")
        
        if(search_name == "name") :
            name = input("please enter your name :")
            for contact in contacts1:
                if contact.name.lower() == name.lower():
                    print("-" *20)
                    print(f"{contacts1.index(contact)+1}) Name: {contact.name}-Email: {contact.email}-Phone: {contact.phone}-Note: {contact.note}")
                    print("-" *20)
                    print("Contact founded successfully!")
                    return
                else :
                    print("Your name is not in the list")

        if(search_name == "email") :
            email = input("please enter your email :")
            for contact in contacts1:
                if contact.email == email:
                    print("-" *20)
                    print(f"{contacts1.index(contact)+1}) Name: {contact.name}-Email: {contact.email}-Phone: {contact.phone}-Note: {contact.note}")
                    print("-" *20)
                    print("Contact founded successfully!")                    
                    return
                else :
                    print("Your email is not in the list")

        if(search_name == "phone") :
            phone = input("please enter your phone :")
            for contact in contacts1:
                if contact.phone == phone:
                    print("-" *20)
                    print(f"{contacts1.index(contact)+1}) Name: {contact.name}-Email: {contact.email}-Phone: {contact.phone}-Note: {contact.note}")
                    print("-" *20)
                    print("Contact founded successfully!")
                    return        
                else :
                    print("Your phone is not in the list")

    # Function to view all contacts
    def view_contacts():
        for contact in contacts1:
            print("-" *20)
            print(f"{contacts1.index(contact)+1}) Name: {contact.name}-Email: {contact.email}-Phone: {contact.phone}-Note: {contact.note}")
            print("-" *20)

    def export_contact():
        filename=input("enter your file name with csv:")
        f = open(filename , "w")
        dict1={}
        if f!="":    
            for contact in contacts1:
                dict1[contact.name]=[contact.email,contact.phone,contact.note]
            f.write(str(dict1))
            print("your file is created .")

                


filename = "/home/ommiamin/teamproject/m98-hw9/contact_manager/data/contacts.pickle"

if os.path.isfile(filename) and os.path.getsize(filename) > 0:
    with open(filename, "rb+") as f:
        try:
            contacts1 = pickle.load(f)
        except EOFError:
            contacts1 = []
else:
    contacts1 = []

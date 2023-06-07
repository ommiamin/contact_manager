
import pickle
import contacts




class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def create_account(self):
        # Implementation for creating a new user account
        pass

    def authenticate(self):
        # Implementation for authenticating a user
        pass

    def change_password(self):
        # Implementation for changing a user's password
        pass







        





# Main loop for the contact management system
while True:
    print("Select an option:")
    print("1. Add a new contact")
    print("2. Edit an existing contact")
    print("3. Delete a contact")
    print("4. View all contacts")
    print("5. Quit")

    option = input("Enter your choice: ")

    if option == "1":
        contacts.Contact.add_contact()
    elif option == "2":
        
        contacts.Contact.edit_contact()
    elif option == "3":
        contacts.Contact.delete_contact()
    elif option == "4":
        contacts.Contact.view_contacts()
    elif option == "5":
        break
    else:
        print("Invalid option. Please try again.")





# Save contacts to a file
with open("/home/ommiamin/teamproject/m98-hw9/contact_manager/data/contacts.pickle", "wb") as f:
    pickle.dump(contacts.contacts1, f)



# Save users to a file
# with open("\data\users.pickle", "wb") as f:
#     pickle.dump(users, f)

# # Load users from a file
# with open("\data\users.pickle", "rb") as f:
#     users = pickle.load(f)


print("end")

import pickle
import contacts
import users

  

# Main loop for the contact management system
while True:
    print("Select an option:")
    print(" 1. create a new user")
    print(" 2. authenticate and enter to contact")
    print(" 3. change password")
    print(" 4. Quit for save new user")
    print("")
    
    option = input("Enter your choice: ")

    if option == "1":
        users.User.create_account()
    elif option == "2":
        if (users.User.authenticate()):
            # Main loop for the contact management system
            while True:
                print("   Select an option:")
                print("     1. Add a new contact")
                print("     2. Edit an existing contact and add note")
                print("     3. Delete a contact")
                print("     4. View all contacts")
                print("     5. search contact")
                print("     6. Export to csv file")
                print("     7. Back")

                option = input("   Enter your choice: ")

                if option == "1":
                    contacts.Contact.add_contact()
                elif option == "2":
                    contacts.C2ontact.edit_contact()
                elif option == "3":
                    contacts.Contact.delete_contact()
                elif option == "4":
                    contacts.Contact.view_contacts()
                elif option == "5" :
                    contacts.Contact.search_contact()
                elif option == "6":
                    contacts.Contact.export_contact()
                elif option == "7":
                    break
                else:
                    print("Invalid option. Please try again.")
        else:
            print("you dont have username and password !" )  

    elif option == "3":
        users.User.change_password()
    elif option == "4":
        break

    else:
        print("Invalid option. Please try again.")





# Save contacts to a file
with open("/home/ommiamin/teamproject/m98-hw9/contact_manager/data/contacts.pickle", "wb") as f:
    pickle.dump(contacts.contacts1, f)



# Save users to a file
with open("/home/ommiamin/teamproject/m98-hw9/contact_manager/data/users.pickle", "wb") as f:
    pickle.dump(users.contacts2 , f)




print("end")
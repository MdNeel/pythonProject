import add_contact
import delete_contact
import view_contacts
import save_file

def main():
    contacts = save_file.load_contacts()

    while True:
        print("\nWelcome to Contact Management System")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Delete Contact")
        print("4. Exit")

        choice = input("Please choose an option: ")

        if choice == "1":
            add_contact.add_contact(contacts)
        elif choice == "2":
            view_contacts.view_contacts(contacts)
        elif choice == "3":
            delete_contact.delete_contact(contacts)
        elif choice == "4":
            print("Thanks for choosing Contact Management System.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()


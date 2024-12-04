
import save_file  # Import save_file for saving updated contacts after deletion.

def delete_contact(contacts):
    """
    Deletes a contact by name.
    """
    name_to_delete = input("Enter the name of the contact to delete: ")

    # Search for the contact by name.
    for name, info in list(contacts.items()):
        if name.lower() == name_to_delete.lower():
            del contacts[name]  # Remove the contact from the dictionary
            save_file.save_contacts(contacts) # Save the updated data after deleting
            print(f"Contact '{name_to_delete}' deleted successfully.")
            return

    # If contact is not found.
    print(f"Error: Contact with name '{name_to_delete}' not found.")

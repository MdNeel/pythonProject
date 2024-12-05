# pythonProject
# Project:Contact Book Management System

The goal of this project is to add contact information, such as name, phone number, email and address. 
ability to save added information the in the file.
ability to delete a contact information from the management system and save the updated information in file after deleting a contact. 
Display all the contact information available in the contact book management system. 
Ability to have user's choice manu to ask user which task user wants to perform. 


Md Neel
Project: Contact Management System

Contact Management System Program Execution Order Step by Step
1.	main.py (Entry Point)
  •	The execution starts here.
  •	This script initializes the program, loads contacts from the file (save_file.py), and displays the menu.
  •	Based on the user’s choice, it calls the appropriate module to perform the required action.
________________________________________
2.	save_file.py (Load Contacts)
  •	As the first step, main.py calls the load_contacts() function from save_file.py.
  •	This function reads the contacts.csv file (or contacts.txt) to load saved contacts into the dictionary structure in     memory.
  •	If the file is empty or invalid, it handles the issue gracefully (e.g., by skipping invalid lines or initializing an empty dictionary).
________________________________________
3.	User's Menu Selection in main.py
  •	After loading contacts, the program displays the menu to the user.
  •	The user selects one of the following options:
    1.	Add Contact: Calls add_contact() from add_contact.py.
    2.	View Contacts: Calls view_contacts() from view_contacts.py.
    3.	Delete Contact: Calls delete_contact() from delete_contact.py.
    4.	Exit: Terminates the program.
________________________________________
4.	add_contact.py (If User Selects "Add Contact")
  •	The add_contact() function is executed when the user chooses to add a new contact.
  •	This function:
    	Validates user input for the name, phone, email, and address.
    	Ensures no duplicate names or phone numbers exist.
    	Updates the contacts dictionary with the new contact.
    	Calls the save_contacts() function from save_file.py to save the updated contacts to the file.
________________________________________
5.	view_contacts.py (If User Selects "View Contacts")
  •	The view_contacts() function is executed when the user wants to see all saved contacts.
  •	It reads the contacts dictionary and formats the data into a clean table.
  •	The formatted data is displayed in the terminal.
________________________________________
6.	delete_contact.py (If User Selects "Delete Contact")
  •	The delete_contact() function is executed when the user wants to remove a contact.
  •	This function:
    	Prompts the user to enter the name of the contact to delete.
    	Searches the contacts dictionary for the matching name.
    	If found, deletes the contact and updates the dictionary.
    	Calls save_contacts() from save_file.py to save the updated data back to the file.
________________________________________
7.	save_file.py (Save Contacts)
  •	Whenever a modification is made to the contacts (e.g., adding or deleting), the save_contacts() function from   save_file.py is called.
  •	This function writes the current state of the contacts dictionary back to the file (contacts.csv).


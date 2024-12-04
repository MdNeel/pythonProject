import save_file
def add_contact(contacts):
    name_key= None
    # Input validation for name
    while True:
        name = input("Enter Name: ").strip()
        if not name.replace(" ", "").isalpha():  # Check if name contains only letters and spaces
            print("Invalid input. Name must contain only letters and spaces.")
            continue

        # Use lowercase for consistent key format for names
        name_key = name.lower()

        # Check for duplicate name
        if name_key in contacts:
            print("Error: A contact with this name already exists. Please enter a different name.")
        else:
            break  # Exit the loop if the name is valid and unique

    # Input validation for phone number
    while True:
        phone = input("Enter Phone: ").strip()
        if not phone.isdigit():  # To ensure that phone number contains only digits
            print("Invalid input. Phone number must contain only digits.")
            continue

        # Check for duplicate phone number
        if any(info["Phone"] == phone for info in contacts.values()):
            print("Error: A contact with this phone number already exists. Please enter a different phone number.")
        else:
            break  # Exit the loop if the phone number is valid and unique

    # Input validation for email
    email = input("Enter Email: ").strip()  # Email validation can be more complex; keeping it simple here

    # Input validation for address
    address = input("Enter Address: ").strip()

    # Add the new contact to the dictionary
    contacts[name_key] = {
        "Phone": phone,
        "Email": email,
        "Address": address
    }

    # Save the updated contacts
    save_file.save_contacts(contacts)
    print("Contact added successfully!")





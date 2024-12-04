import save_file
def add_contact(contacts):
    name = input("Enter Contact Name: ").strip()
    phone_num = input("Enter Phone Number: ").strip()
    email = input("Enter Email Address: ").strip()
    address = input("Enter Contact's Address: ").strip()

    name_key = name.lower()  # Use lowercase for consistent key format.

    if name_key in contacts:
        print("Error: A contact with this name already exists!")
        return

    contacts[name_key] = {
        "Phone": phone_num,
        "Email": email,
        "Address": address
    }
    save_file.save_contacts(contacts)
    print("Contact added successfully!")


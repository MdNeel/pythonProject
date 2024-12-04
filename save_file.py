import json
import csv

def save_contacts(contacts):
    """
    Saves all contacts to a CSV file.
    """
    with open("contacts.csv", "w", newline="") as file:  # Save as contacts.csv
        writer = csv.writer(file)  # Use CSV writer for safe saving.
        for name, info in contacts.items():
            writer.writerow([name, info["Phone"], info["Email"], info["Address"]])


def load_contacts():
    """
    Loads contacts from a CSV file.
    Returns a dictionary of contacts.
    """
    contacts = {}
    try:
        with open("contacts.csv", "r") as file:  # Load from contacts.csv
            reader = csv.reader(file)  # Use CSV reader for safe parsing.
            for line in reader:
                # Ensure valid data structure for each line.
                if len(line) == 4:
                    name, phone, email, address = line
                    contacts[name] = {"Phone": phone, "Email": email, "Address": address}
                else:
                    print(f"Skipping invalid line: {','.join(line)}")
    except FileNotFoundError:
        print("No saved contacts found. Starting fresh.")

    return contacts


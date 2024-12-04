def view_contacts(contacts):
    """
    Displays all saved contacts in a formatted table without using any external libraries.
    """
    if not contacts:
        print("No contacts to display.")
        return

    # Define headers
    headers = ["S.N0", "NAME", "ADDRESS", "EMAIL", "PHONE_NUMBER"]

    # Calculate column's widths
    col_widths = [len(header) for header in headers]
    rows = []

    for idx, (name, info) in enumerate(contacts.items(), start=1):
        row = [str(idx), name, info["Address"], info["Email"], info["Phone"]]
        rows.append(row)

        # Update column widths to fit the longest content
        col_widths = [max(col_widths[i], len(row[i])) for i in range(len(headers))]

    # Create a horizontal line
    line = "+".join("-" * (width + 2) for width in col_widths)
    line = f"+{line}+"

    # Print the table
    print(line)
    print("| " + " | ".join(header.ljust(col_widths[i]) for i, header in enumerate(headers)) + " |")
    print(line)

    for row in rows:
        print("| " + " | ".join(row[i].ljust(col_widths[i]) for i in range(len(row))) + " |")
    print(line)


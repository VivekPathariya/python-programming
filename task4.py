# Welcome message and initialization
print("Welcome to the Contact Book!")

# Contact storage
contacts = []  # List to store contact dictionaries

while True:
    # Display menu
    print("\nMenu:")
    print("1. Add Contact")
    print("2. View Contact List")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")
    
    # Get user choice
    choice = input("Choose an option (1-6): ")
    
    if choice == "1":  # Add Contact
        print("\nAdd Contact:")
        name = input("Enter Name: ")
        phone = input("Enter Phone Number: ")
        email = input("Enter Email (optional): ")
        address = input("Enter Address (optional): ")
        
        # Store contact details in a dictionary
        contact = {"name": name, "phone": phone, "email": email, "address": address}
        contacts.append(contact)
        print(f"Contact '{name}' added successfully!")
    
    elif choice == "2":  # View Contact List
        print("\nContact List:")
        if not contacts:
            print("No contacts found!")
        else:
            for idx, contact in enumerate(contacts, start=1):
                print(f"{idx}. {contact['name']} - {contact['phone']}")
    
    elif choice == "3":  # Search Contact
        print("\nSearch Contact:")
        search_term = input("Enter name or phone number to search: ").lower()
        found = False
        for contact in contacts:
            if search_term in contact["name"].lower() or search_term in contact["phone"]:
                print(f"\nName: {contact['name']}")
                print(f"Phone: {contact['phone']}")
                print(f"Email: {contact['email']}")
                print(f"Address: {contact['address']}")
                found = True
        if not found:
            print("No contact found with that name or phone number!")
    
    elif choice == "4":  # Update Contact
        print("\nUpdate Contact:")
        update_name = input("Enter the name of the contact to update: ").lower()
        for contact in contacts:
            if contact["name"].lower() == update_name:
                print(f"Current details: {contact}")
                contact["name"] = input(f"Enter new name (or press Enter to keep '{contact['name']}'): ") or contact["name"]
                contact["phone"] = input(f"Enter new phone number (or press Enter to keep '{contact['phone']}'): ") or contact["phone"]
                contact["email"] = input(f"Enter new email (or press Enter to keep '{contact['email']}'): ") or contact["email"]
                contact["address"] = input(f"Enter new address (or press Enter to keep '{contact['address']}'): ") or contact["address"]
                print("Contact updated successfully!")
                break
        else:
            print("No contact found with that name!")
    
    elif choice == "5":  # Delete Contact
        print("\nDelete Contact:")
        delete_name = input("Enter the name of the contact to delete: ").lower()
        for contact in contacts:
            if contact["name"].lower() == delete_name:
                contacts.remove(contact)
                print(f"Contact '{contact['name']}' deleted successfully!")
                break
        else:
            print("No contact found with that name!")
    
    elif choice == "6":  # Exit
        print("\nThank you for using the Contact Book!")
        break
    
    else:
        print("Invalid choice! Please try again.")

import json
import os

DATA_FILE = "contacts.json"


def load_contacts():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as f:
            return json.load(f)
    return []


def save_contacts(contacts):
    with open(DATA_FILE, 'w') as f:
        json.dump(contacts, f, indent=4)


def add_contact(contacts):
    print("\n--- Add New Contact ---")
    name = input("Name: ").strip()
    phone = input("Phone number: ").strip()
    email = input("Email: ").strip()
    address = input("Address: ").strip()

    contact = {
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    }
    contacts.append(contact)
    save_contacts(contacts)
    print(f"Contact '{name}' added successfully.")


def view_contacts(contacts):
    print("\n--- Contact List ---")
    if not contacts:
        print("No contacts saved yet.")
        return

    for i, c in enumerate(contacts, start=1):
        print(f"{i}. {c['name']} - {c['phone']}")


def find_matches(contacts, query):
    query = query.lower()
    return [c for c in contacts if query in c['name'].lower() or query in c['phone']]


def search_contact(contacts):
    print("\n--- Search Contact ---")
    query = input("Enter name or phone number to search: ").strip()
    matches = find_matches(contacts, query)

    if not matches:
        print("No matching contacts found.")
        return

    print(f"Found {len(matches)} match(es):")
    for i, c in enumerate(matches, start=1):
        print(f"{i}. Name: {c['name']}")
        print(f"   Phone: {c['phone']}")
        print(f"   Email: {c['email']}")
        print(f"   Address: {c['address']}")


def update_contact(contacts):
    print("\n--- Update Contact ---")
    query = input("Enter name or phone number of contact to update: ").strip()
    matches = find_matches(contacts, query)

    if not matches:
        print("No matching contacts found.")
        return

    if len(matches) > 1:
        print("Multiple matches found:")
        for i, c in enumerate(matches, start=1):
            print(f"{i}. {c['name']} - {c['phone']}")
        try:
            choice = int(input("Select the number of the contact to update: "))
            contact = matches[choice - 1]
        except (ValueError, IndexError):
            print("Invalid selection.")
            return
    else:
        contact = matches[0]

    print(f"Updating contact: {contact['name']}")
    print("Leave field blank to keep the current value.")

    new_name = input(f"Name [{contact['name']}]: ").strip()
    new_phone = input(f"Phone [{contact['phone']}]: ").strip()
    new_email = input(f"Email [{contact['email']}]: ").strip()
    new_address = input(f"Address [{contact['address']}]: ").strip()

    if new_name:
        contact['name'] = new_name
    if new_phone:
        contact['phone'] = new_phone
    if new_email:
        contact['email'] = new_email
    if new_address:
        contact['address'] = new_address

    save_contacts(contacts)
    print("Contact updated successfully.")


def delete_contact(contacts):
    print("\n--- Delete Contact ---")
    query = input("Enter name or phone number of contact to delete: ").strip()
    matches = find_matches(contacts, query)

    if not matches:
        print("No matching contacts found.")
        return

    if len(matches) > 1:
        print("Multiple matches found:")
        for i, c in enumerate(matches, start=1):
            print(f"{i}. {c['name']} - {c['phone']}")
        try:
            choice = int(input("Select the number of the contact to delete: "))
            contact = matches[choice - 1]
        except (ValueError, IndexError):
            print("Invalid selection.")
            return
    else:
        contact = matches[0]

    confirm = input(f"Are you sure you want to delete '{contact['name']}'? (y/n): ").strip().lower()
    if confirm in ('y', 'yes'):
        contacts.remove(contact)
        save_contacts(contacts)
        print("Contact deleted successfully.")
    else:
        print("Deletion cancelled.")


def print_menu():
    print("\n" + "=" * 35)
    print("           CONTACT BOOK")
    print("=" * 35)
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")


def contact_book():
    contacts = load_contacts()

    while True:
        print_menu()
        choice = input("Choose an option (1-6): ").strip()

        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            view_contacts(contacts)
        elif choice == '3':
            search_contact(contacts)
        elif choice == '4':
            update_contact(contacts)
        elif choice == '5':
            delete_contact(contacts)
        elif choice == '6':
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please choose a number between 1 and 6.")


if __name__ == "__main__":
    contact_book()

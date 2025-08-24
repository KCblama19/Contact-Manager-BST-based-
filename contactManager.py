class ContactNode:
    def __init__(self, name: str, phone, email: str = None, address: str = None) -> None:
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address
        self.leftContact = None
        self.rightContact = None

class ContactManager:
    def __init__(self):
        self.rootContact = None

    # -------- Utility Printing --------
    def printContact(self):
        print("\n----- Contact List -----")
        if not self.rootContact:
            print("No contacts available.")
            return
        self._printContact(self.rootContact)
    
    def _printContact(self, node: ContactNode):
        if node is None:
            return
        self._printContact(node.leftContact)
        print(f"{node.name} - {node.phone} - {node.email} - {node.address} ")
        self._printContact(node.rightContact)

    # ------------- Insert -------------
    def insert(self, name: str, phone, email: str = None, address: str = None):
        if self.rootContact is None:
            self.rootContact = ContactNode(name, phone, email, address)
            print("Contact Added Successfully")
        else:
            self._insert(self.rootContact, name, phone, email, address)
        
    def _insert(self, currContact, name: str, phone, email: str = None, address: str = None) -> ContactNode:
        if name.lower() < currContact.name.lower():
            if currContact.leftContact is None:
                currContact.leftContact = ContactNode(name, phone, email, address)
                print("Contact added successfully!")
            else:
                self._insert(currContact.leftContact, name, phone, email, address)

        elif name.lower() > currContact.name.lower():
            if currContact.rightContact is None:
                currContact.rightContact = ContactNode(name, phone, email, address) 
                print("Contact added successfully!")
            else:
                self._insert(currContact.rightContact, name, phone, email, address)

        else:
            print("Contact with this name already exists!")
    
    # ------------- Search -------------
    def search(self, name: str) -> ContactNode:
        return self._search(self.rootContact, name.lower())

    def _search(self, node: ContactNode, name: str) -> ContactNode:
        if node is None:
            return None
        
        if name == node.name.lower():
            return node
        elif name < node.name.lower():
            return self._search(node.leftContact, name)
        else:
            return self._search(node.rightContact, name)

    # ------------- Update -------------
    def update(self, name:str, phone, email:str = None, address:str = None):
        node = self.search(name)
        if node:
            if phone:
                node.phone = phone
            if email:
                node.email = email
            if address:
                node.address = address
            return node
        return None
    
    # ------------- Delete -------------
    def get_successor(self, curr: ContactNode):
        curr = curr.rightContact
        while curr is not None and curr.leftContact is not None:
            curr = curr.leftContact
        return curr
    
    def delete(self, name:str) -> bool:
        deleted, self.rootContact = self._delete(self.rootContact, name.lower())
        return deleted
    
    def _delete(self, node: ContactNode, name:str) -> ContactNode:
        if node is None:
            return False, None
        
        # If key to be searched is in a subtree(right or left subtree)
        if name.lower() < node.name.lower():
            deleted, node.leftContact = self._delete(node.leftContact, name)
            return deleted, node # Node was deleted
        elif name.lower() > node.name.lower():
            deleted, node.rightContact = self._delete(node.rightContact, name)
            return deleted, node
        else:
            # Node with only one child or no child
            if node.leftContact is None:
                return True, node.rightContact # Node was deleted
            if not node.rightContact:
                return True, node.leftContact
            
            # Node with two children, get the in-order successor
            succ = self.get_successor(node)
            node.name, node.phone, node.email, node.address = succ.name, succ.phone, succ.email, succ.address
            deleted, node.rightContact = self._delete(node.rightContact, succ.name)
            return True, node

class ContactManagerApp:
    def __init__(self):
        self.myContact = ContactManager()

    # Validate user input:
    def get_valid_input(self, prompt: str, expected_type: type, error_message: str, required: bool = True):
        while True:
            try:
                value = input(prompt).strip()

                if not value and not required:
                    return None
                
                if expected_type == str:
                    if not value and required:  # avoid empty strings
                        raise ValueError("Empty value not allowed")
                    return value   # keep string
                    
                else:
                    raise TypeError("Unsupported type") 
                
            except ValueError:
                print(error_message)

    def run(self):
        while True:
            print("\nHello Welcome to Contact Book.")
            print("1. Add Contact")
            print("2. Search Contact")
            print("3. Update Contact")
            print("4. Delete Contact")
            print("5. Display All Contacts")
            print("6. Exit")

            try:
                option = int(input("> ").strip())
            except ValueError:
                print("Invalid input. Please enter 1-6.")
                continue

            match option:
                case 1:
                    # Validate inputs before calling the add method
                    name = self.get_valid_input("Enter name: ", str, "Invalid value, must be a string", required=True)
                    phone = self.get_valid_input("Enter Phone: ", str, "Invalid value, must be an integer", required=True)
                    email = self.get_valid_input("Enter Email (optional): ", str, "Invalid value, must be a string", required=False)
                    address = self.get_valid_input("Enter Address (optional): ", str, "Invalid value, must be a string", required=False) 

                    # Add the contact
                    self.myContact.insert(name, phone, email, address)

                case 2:
                    # Validate inputs is a string before searching
                    name = self.get_valid_input("Enter Contact name to Search: ", str, "Invalid value, must be a string")
                    contactFound = self.myContact.search(name)
                    # Validate the contact was found
                    if contactFound:
                        print(f"{contactFound.name} - {contactFound.phone} - {contactFound.email} - {contactFound.address}")
                    else:
                        print("Contact does not exist")
                
                case 3:
                    name = self.get_valid_input("Enter name of Contact to Update: ", str, "Invalid value, must be a string", required=True)
                    phone = self.get_valid_input("Enter Updated Phone: ", str, "Invalid value, must be an integer", required=True)
                    email = self.get_valid_input("Enter Updated Email (optional): ", str, "Invalid value, must be a string", required=False)
                    address = self.get_valid_input("Enter Updated Address (optional): ", str, "Invalid value, must be a string", required=False)

                    contactUpdated = self.myContact.update(name, phone, email, address)
                    if contactUpdated:
                        print(f"\nThe Contact {contactUpdated.name} was Updated, new details below")
                        print(f"Name: {contactUpdated.name}\n"
                            f"Phone:{contactUpdated.phone}\n"
                            f"Email: {contactUpdated.email}\n"
                            f"Address: {contactUpdated.address}")
                    else:
                        print(f"\nThe Contact '{name}' could not be found")

                case 4:
                    # Validate inputs is a string before searching
                    name = self.get_valid_input("Enter Contact name to Search: ", str, "Invalid value, must be a string")
                    deleted = self.myContact.delete(name)
                    # Validate the contact was deleted
                    if deleted:
                        print(f"'{name}' deleted successfully")
                    else:
                        print("Contact does not exist")

                case 5:
                    self.myContact.printContact()

                case 6:
                    try:
                        confirm = str(input("Wanna leave(y/n)): ").strip().lower())
                    except ValueError:
                        print("Please enter a valid value")

                    if confirm == y:
                        print("GoodBye!")
                        break
                    else:
                        continue


if __name__ == "__main__":
    ContactManagerApp().run()
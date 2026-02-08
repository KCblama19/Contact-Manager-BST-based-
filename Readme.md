# Contact Manager (BST-based)

A console-based **Contact Manager** that stores and manages contacts using a **Binary Search Tree (BST)** for efficient searching by name.  
This project demonstrates how data structures can be applied to real-world problems, focusing on **insertion, searching, updating, and deletion** of contacts.

## Features

- Add new contacts (name, phone, email, address)
- Search for a contact by name (efficient BST lookup)
- Update existing contact details
- Delete a contact
- Display all contacts in alphabetical order (in-order BST traversal)
- Input validation to ensure clean and structured data

## Technologies Used

- **Language**: Python 3
- **Data Structure**: Binary Search Tree (BST)

## Project Structure

```bash
ContactManager/
│── contact_manager.py # Main program logic
│── README.md # Project documentation
```

## How It Works

1. Each contact is stored as a node in the BST.

   - **Key**: Contact Name (used for ordering)
   - **Value**: Phone, Email, Address

2. Operations supported:
   - **Insert**: Add a new contact into the BST.
   - **Search**: Find contact details by name.
   - **Update**: Modify an existing contact’s details.
   - **Delete**: Remove a contact from the BST.
   - **Traverse**: List all contacts alphabetically.

## Setup & Run (Beginner-Friendly)

### 1. Install Python

Make sure Python 3 is installed on your computer.  
You can download it from: [https://www.python.org/downloads/](https://www.python.org/downloads/)

Check installation:

```bash
python --version
```

### 2. Clone the Project

```bash
git clone https://github.com/your-username/contact-manager-bst.git
cd contact-manager-bst
```

### 3. Run the program:

```bash
python contact_manager.py
```

### 4. Use the Menu:

Follow the console menu to:

- Add a contact
- Search a contact
- Update a contact
- Delete a contact
- Display all contacts
- Exit the program

### Example Run

```bash
===== Contact Manager =====
1. Add Contact
2. Search Contact
3. Update Contact
4. Delete Contact
5. Display All Contacts
6. Exit
Enter choice: 1

Enter name: John Doe
Enter phone: 123456789
Enter email: john@example.com
Enter address: 123 Main St
Contact added successfully!
```

## Future Improvements

- Save contacts to a file(persistent storage)
- Load contacts at startup
- GUI version(Tkinter or web-based)
- Balance BST using AVL Tree or Red-Black Tree for optimal efficiency
- Add contact groups and tags

## Learning Goals

This project helped reinforce:

- Implementation of BST operations
- Practical application of DSA concepts
- Error handling and input validation
- Designing a real-world mini-application

## Author

- Abraham K.C Blama(I'm thinking of nicknaming myself **Round-Robin**)
- Wanna see more of my projects come here: [KCblama19](https://github.com/KCblama19)  
- Contact me at: [Roubin-Robin-Mail](abrahamablama19@gmail.com)
```bash  
For context: Round-Robin(scheduling algorithm) is one of the fairest algorithm in computer science, it balances every tasks in the CPU so that each task gets a turn to be executed and I like to live that way too: balanced, fair, and making sure no one in my cycle gets left out, but, with a twist, I don't let anyone hog my time, lol, so basically, I would check-in, keep things moving and move to the next person.  
```

# Creating a class called "Contact" which will store all the information required for one contact to be created in my contact book e.g. name, phone number, email address etc.
class Contact:
    def __init__(self, first_name, last_name, email, country_code, phone_number, city): # Outlining the attributes of the class Contact
        self.first_name = first_name # This ensures for each specific object that the first name is stored in the attribute first_name
        self.last_name = last_name # This ensures for each specific object that the last name is stored in the attribute last_name
        self.email = email # This ensures for each specific object that the email is stored in the attribute email
        self.country_code = country_code # This ensures for each specific object that the country code is stored in the attribute country_code
        self.phone_number = phone_number # This ensures for each specific object that the phone number is stored in the attribute phone_number
        self.city = city # This ensures for each specific object that the city is stored in the attribute city

    def __str__(self): # This is a sepcial dunder method like __init__ that python understands and is used to help control the formatting of how objects are printed out when the print() function is called on them. This method is used to return a string representation of the object.
        return f"{self.first_name}, {self.last_name}, {self.email}, {self.country_code}, {self.phone_number}, {self.city}" # so this will print something like "John, Doe, john.doe@example.com, +1, 123-456-7890, New York"

valid_field_names = {
                        "first name": "first_name", 
                        "last name":"last_name", 
                        "email": "email", 
                        "email address": "email",
                        "country code": "country_code",
                        "phone number": "phone_number", 
                        "city": "city"
                        } # This is a list of valid field names that can be updated in the contact book


# Helper functions get_valid_phone_number, get_real_field_name

def get_valid_phone_number(): # This is a function that will validate a users input for phone number and check it is less than 15 digits longs and contains only digits. If it does then the function will return the valid phone number. If it doesnt then the user will prompted to enter a valid phone number again. if the user inouts exit or cancel then the function will return None and None will be passed into the respective wider fucntion which will stop that wider function from continuing
    while True: # This will loop the code below until a valid phone number is given or the user inputs exit or cancel
        phone_number = input("Enter a phone number: ") # This will prompt the user to enter a phone number
        if phone_number.lower() == "cancel" or phone_number.lower() == "exit": # This checks if the user wants to cancel or exit the program. If they do, then the program will return to the main menu and not remove any contacts.
            print("Adding contact operation cancelled. Returning to main menu.") # This will print a message to the user that the operation has been cancelled and they are being returned to the main menu
            return None # This will pass None to the fucntion and this will be the input into the wider functiuon to which this function is nested in which will stop all code continuing in the wider function
        if phone_number.isdigit() and len(phone_number) <= 15: # This checks if the phone number is valid by checking if it contains only digits and has 15 or fewer digits
            return phone_number
        else: # If the phone number is not valid, the program will print an error message and the loop will continue
            print("Invalid phone number. Please try again.") # This will print an error message if the phone number is not valid and the while True loop runs again

def get_real_field_name(field_name): # This function will validate whether a user has inputted a valid field to sort, filter, update contactsd by
    if field_name.lower() in valid_field_names: # Checks whether the user has inputted any valid field name from valid_field_name list
        return valid_field_names[field_name.lower()] # Pass back into the function the actual field name with underscore if necessary e.g. when user "phone number", this is now converted to "phone_number"
    else: # this means the user had inputted an invalid field name list that is not found in valid_field_name list
        return None # Pass back into the function None to represent that no user inputted valid field name was found

    
def add_contact(contacts):
    # Step 1: get and validate phone number
    # Adding a program that checks whether the phone number is valid or not. A valid phone number is one that has digits only and has 15 or fewer digits 
    phone_number  = get_valid_phone_number()
    if phone_number is None:
        print("Adding contact operation cancelled. Returning to main menu.") # This will print a message to the user that the operation has been cancelled and they are being returned to the main menu")
        return  # This will return to the main menu and not add any contacts
    # Step 2: check for duplicate phone number
    # Checking for whether the phone number given is already in the contact book or not. If it is, then the program will print an error message and ask the user to enter a different phone number. If it is not, then the program will continue and create a new contact with the given information.

    elif phone_number in contacts: # This checks if the phone number is already in the contact book
        print("This phone number is already in the contact book. Please enter a different phone number.") # This will print an error message if the phone number is already in the contact book
        return # This will return to the beginning of the program and ask the user to enter a different phone number
    else:
        pass

    while True: # This is a while loop that will keep running until the user enters a valid email address
        email = input("Enter email address: ") # This will prompt the user to enter an email address # I need to do a check on this before it is complete to have the "@" symbol submerged in the email address. If it is not, then the program will print an error message and ask the user to enter a different email address. If it is, then the program will continue and create a new contact with the given information.
        if email.count("@") == 1 and email[0] != "@" and email[-1] != "@": # This checks if the email address is valid by checking if it contains exactly one "@" symbol and that the first and last characters are not "@" symbols
            break # If the email address is valid, the loop will break and the program will continue
        else: # if  the email address is not valid, the program will print an error message and the loop will continue
            print("Invalid email address. Please try again.") # This will print an error message if the email address is not valid

    while True:
        country_code = input("Enter country code: ") # This will prompt the user to enter a country code

        if len(country_code) > 0 and country_code[0] == "+": # This checks whether there is more than one character and if the first character of the country code is a "+" symbol or not. If it is, then the program will continue and create a new contact with the given information. If it is not, then the program will print an error message and ask the user to enter a different country code.
            country_code = country_code.strip("+") # This will remove the "+" symbol from the country code if it is present

        if country_code.isdigit(): # This checks whether the country code is made of just numbers or not. If it is, then the program will continue and create a new contact with the given information. If it is not, then the program will print an error message and ask the user to enter a different country code.
            break # If the country code is valid, the loop will break and the program will continue
        else: # if the country code is not valid, the program will print an error message and loop will continue
            print("Invalid country code. Please try again.") # This will print an error message if the country code is not cvalid and the loop will continue


    # Step 3: collect the remaining contact info
    first_name = input("Enter first name: ") # This will prompt the user to enter a first name
    last_name = input("Enter last name: ") # This will prompt the user to enter a last name
    city = input("Enter city: ") # This will prompt the user to enter a city

    user_contact = Contact(first_name, last_name, email, country_code, phone_number, city) # This will create a new contact with the given information
    contacts[phone_number] = user_contact # This will add the new contact to the contact book with the phone number as the key and the contact object as the value

def display_contacts(contacts): # This is a function that will display all the contacts in the contact book
    for contact in contacts.values(): # This will loop through all the contacts in the contact book and print them out
        print(contact) # This will print out the contact information for each contact in the contact book    


def remove_contact(contacts): # This is a function that will remove a contact from the contact book
    phone_number = get_valid_phone_number() #Assigning the rturn value of the function called get_valid_phone_number(). This function validates that the phoine number the user inputs(loops over until a user gives a phone number input) only contains digits and less than 15 digits or return sNone if the user inputs "exit" or "cancel" for the fucntion so that the outer function remove_contacts tops aswell
    if phone_number is None:
        print("Removing contact operation cancelled. Returning to main menu.") # This will print a message to the user that the operation has been cancelled and they are being returned to the main menu
        return  # This will return to the main menu and not remove any contacts
    if phone_number in contacts: # This checks if the phone number is already in the contact book
        removed_contact = contacts.pop(phone_number) # This will remove the contact object by finding the phone number in the contact book and deleting it from the dictionary
        print(f"Contact removed: {removed_contact.first_name} {removed_contact.last_name}") # This will print the first name and last name of the contact removed and show the user
    else: # If the phone number is not in the contact book, then the program will print an error message and ask the user to enter a different phone number.
        print("This phone number doesn't exist in the contact book. Please enter a different phone number") # This will print an error message if the phone number is not in the contact book


def update_contact(contacts): # This is a function that will update a contact in the contact book
    phone_number = get_valid_phone_number() #Assigning the rturn value of the function called get_valid_phone_number(). This function validates that the phoine number the user inputs(loops over until a user gives a phone number input) only contains digits and less than 15 digits or return sNone if the user inputs "exit" or "cancel" for the fucntion so that the outer function remove_contacts tops aswell
    if phone_number is None: # If the get_valid_phone_number() function returns None because the user inputed exit or cancel for phone number to cnacel the operation
        print("Updating contact operation cancelled. Returning to main menu.") # This will print a message to the user that the operation has been cancelled and they are being returned to the main menu
        return  # This will return to the main menu and not update any contacts
        # Step 2: check if phone number already exists in contacts
        # Checking for whether the phone number given is already in the contact book or not. If it is, then the program will ask for the user to enter the field they want toi update and then ask for the new value of that field. If it is not, then the program will print an error message and ask the user to enter a different phone number.
        
    if phone_number in contacts: # This checks if the phone number is already in the contact book
        while True: # This is a while loop that will keep running until the user enters a valid field name
            field_name = input("Enter the field name you would like to update: ") # This will prompt the user to enter the field name they would like to update
            if field_name.lower() == "cancel" or field_name.lower() == "exit": # This checks if the user wants to cancel or exit the program. If they do, then the program will return to the main menu and not remove any contacts.
                print("Updating contact operation cancelled. Returning to main menu.") # This will print a message to the user that the operation has been cancelled and they are being returned to the main menu
                return # This will return to the main menu and not remove any contacts
            real_field_name = get_real_field_name(field_name) #Stores the result of the function that validates whether a user has inputted a valid field name or not. Returns either the valid field name with underscores if needed e.g. user inputs "phone number" converted to actual field name variable "phone_number". if not vaslid field name given it returns None
            if real_field_name is not None: # This checks the user inputs a valid field name first
                if real_field_name == "phone_number": # branch based on the REAL name, not the raw input
                    contact = contacts.pop(phone_number) # This will remove the contact object by finding the phone number in the contact book and deleting it from the dictionary
                    new_phone_number = get_valid_phone_number() # This will validate the new phone number the user gives, looping until it is valid digits and 15 or fewer characters, or returning None if the user cancels or exits

                    if new_phone_number is None: # If the user cancelled or exited while entering the new phone number
                       print("Updating the phone number of the contact operation cancelled. Returning to main menu.") # This will print a message to the user that the operation has been cancelled and they are being returned to the main menu
                       contacts[phone_number] = contact # This restores the contact object back into the dictionary under its original phone number key, since it was popped out earlier and would otherwise be lost if the operation is cancelled here
                       return # This will return to the main menu and not update the contact
                    else: # If a valid new phone number was given
                        contact.phone_number = new_phone_number # This will update the phone number attribute of the contact object to the new phone number given by the user
                        contacts[new_phone_number] = contact # This will add the contact back into the dictionary under the new phone number as the key
                        print(f"Phone number updated to {new_phone_number}.") # This will print a message to the user that the phone number has been updated to the new phone number given
                        return # This will return to the main menu after successfully updating the phone number
                else: # This checks if the field name is any other valid non phone number field 
                    new_value = input(f"Enter the new value for {field_name}: ") # This will prompt the user to enter the new value for the field name they would like to update
                    setattr(contacts[phone_number], real_field_name, new_value) # This will update the value of the field name in the contacts object that the user entered the phopne number for. The update value will be whatever the user inputted as the new value for that field name. The setattr() function is a built-in function in Python that allows you to set the value of an attribute of an object. The first argument is the object, the second argument is the name of the attribute, and the third argument is the new value for that attribute.
            else: # If the field name is not valid, the program will print an error message and the loop will continue
                print("Invalid field name. Pleae check you have spelled the filed name correctly. Please try again.") # This will print an error message if the field name is not valid
    else: # If the phone number is not in the contact book, then the program will print an error message and ask the user to enter a different phone number.
        print("This phone number doesn't exist in the contact book. Please enter a different phone number") # This will print an error message if the phone number is not in the contact book
        return # This will return to the beginning of the program and ask the user to enter a different phone number

def filter_contacts(contacts): # This is a function that filters contacts by the value a user gives to them. The user will be prompted to enter a value and the program will filter the contacts by that value and print out the contacts that match that value.
    filter_field_name = input("Enter the field name you would like to filter by: ") # This will prompt the user to enter the field name the user weould like to filter by 
    filter_value = input("Enter the value you would like to filter by: ") # This will prompt the user to enter the value they would like to filter by
    if filter_field_name.lower() == "cancel" or filter_field_name.lower() == "exit" or filter_value.lower() == "cancel" or filter_value.lower() == "exit": # This checks if the user wants to cancel or exit the program. If they do, then the program will return to the main menu and not filter any contacts.
        print("Filtering contacts operation cancelled. Returning to main menu.") # This will print a message to the user that the operation has been cancelled and they are being returned to the main menu
        return # This will return to the main menu and not remove any contacts
    real_filter_field_name = get_real_field_name(filter_field_name) #Stores the result of the function that validates whether a user has inputted a valid field name or not. Returns either the valid field name with underscores if needed e.g. user inputs "phone number" converted to actual field name variable "phone_number". if not vaslid field name given it returns None
    if real_filter_field_name is None: # This checks if the field name is valid by checking if it is in the list of valid field names
        print("Invalid field name. Please try again.") # This will print an error message if the field name is not valid
    else: # If the field name is valid, the program will filter the contacts by the value the user entered and print out the contacts that match that value.
        match_found = False # This is a boolean variable that will be used to check if a match is found or not. It is set to False by default and will be set to True if a match is found.
        for contact in contacts.values(): # This will loop through all the contacts in the contact book and print them out
            if getattr(contact, real_filter_field_name) == filter_value: # This checks if the value of the field name in the contacts object matches currently existing value the user entered. If it does, then the program will print out the contact of the object or objects containing the matching value.
                print(contact) # This will print out the contact information for each contact in the contact book that matches the value the user entered
                match_found = True # This will set the match_found variable to True if a match is found
        if match_found == False: # This checks if a match was found or not. If it was not, then the program will print out a message to the user that no matches were found.
            print("No matches found.") # This will print out a message to the user that no matches were found

def sort_contacts(contacts): # This is a function that sorts contacts by the value a user gives to them. The user will be prompted to enter a value and the program will sort the contacts by that value and print out the contacts in sorted order.
    contact_list = list(contacts.values()) # This will create a list of all the contacts in the contact book
    sort_field_name = input("Enter the field name you would like to sort by: ") # This will prompt the user to enter the field name the user would like to sort by
    if sort_field_name.lower() == "cancel" or sort_field_name.lower() == "exit": # This checks if the user wants to cancel or exit the program. If they do, then the program will return to the main menu and not sort any contacts.
        print("Sorting contacts operation cancelled. Returning to main menu.") # This will print a message to the user that the operation has been cancelled and they are being returned to the main menu
        return # This will return to the main menu and not sort any contacts

    real_sort_field_name = get_real_field_name(sort_field_name) #Stores the result of the function that validates whether a user has inputted a valid field name or not. Returns either the valid field name with underscores if needed e.g. user inputs "phone number" converted to actual field name variable "phone_number". if not vaslid field name given it returns None
    if real_sort_field_name is None: # This checks if the field name is valid by checking if it is in the list of valid field names
        print("Invalid field name. Please try again.") # This will print an error message if the field name is not valid
        return # This will return to the main menu and not sort any contacts
    else: # If the field name is valid, the program will sort the contacts by the value the user entered and print out the contacts in sorted order.
        while True: # This is a while loop that will keep running until the user enters a valid option
            reverse_order_answer = input(f"How would you like to sort your contacts by {real_sort_field_name}? /nA. A-Z /nB. Z-A") # This will prompt the user to enter how they would like to sort their contacts by the field name they entered. The user can enter A for ascending order or B for descending order. The program will then sort the contacts by the field name in the order the user entered and print out the contacts in sorted order.
            if reverse_order_answer.lower() == "cancel" or reverse_order_answer.lower() == "exit": # This checks if the user wants to cancel or exit the program. If they do, then the program will return to the main menu and not sort any contacts.
                print("Sorting contacts operation cancelled. Returning to main menu.") # This will print a message to the user that the operation has been cancelled and they are being returned to the main menu
                return # This will return to the main menu and not sort any contacts
            elif reverse_order_answer.lower() == "a" or reverse_order_answer.lower() == "a. a-z" or reverse_order_answer.lower() == "a. a to z" or reverse_order_answer.lower() == "a-z" or reverse_order_answer.lower() == "a to z" or reverse_order_answer.lower() == "acending" or reverse_order_answer.lower() == "ascending order": # This checks if the user wants to sort the contacts in ascending order. If they do, then the program will sort the contacts by the field name in ascending order and print out the contacts in sorted order.
                reverse_order = False # This will set the reverse_order variable to False if the user wants to sort the contacts in ascending order    
                contact_list = sorted(contact_list, key = lambda contact: getattr(contact, real_sort_field_name), reverse=reverse_order) # This will sort the list of contacts by the value of the field name in the contacts object that the user entered. The lambda function is used to create an anonymous function that takes a contact object as an argument and returns the value of the field name in that contact object.
                break # This will break the loop and the program will continue
            elif reverse_order_answer.lower() == "b" or reverse_order_answer.lower() == "b. z-a" or reverse_order_answer.lower() == "b. z to a" or reverse_order_answer.lower() == "z-a" or reverse_order_answer.lower() == "z to a" or reverse_order_answer.lower() == "descending" or reverse_order_answer.lower() == "descendng order": # This checks if the user wants to sort the contacts in descending order. If they do, then the program will sort the contacts by the field name in descending order and print out the contacts in sorted order.
                reverse_order = True # This will set the reverse_order variable to True if the user wants to sort the contacts in descending order
                contact_list = sorted(contact_list, key = lambda contact: getattr(contact, real_sort_field_name), reverse=reverse_order) # This will sort the list of contacts by the value of the field name in the contacts object that the user entered. The lambda function is used to create an anonymous function that takes a contact object as an argument and returns the value of the field name in that contact object.
                break # This will break the loop and the program will continue
            else: # If the user enters an invalid option, the program will print an error message and return to the main menu.
                print("Invalid option. Please try again.") # This will print an error message if the user enters an invalid option
        for contact in contact_list: # This will loop through all the contacts in the sorted list and print them out
            print(contact) # This will print out the contact information for each contact in the sorted list

commands = {
    "add": add_contact,
    "add contact": add_contact,
    "add a contact": add_contact,
    "add to contacts": add_contact,
    "add to my contacts": add_contact,
    "add to my contacts book": add_contact,
    "add contacts": add_contact,
    "add contact to contact book": add_contact,
    "add a contact to contact book": add_contact,
    "add contacts to contact book": add_contact,
    "add a contact to my contact book": add_contact,
    "add contacts to my contact book": add_contact,
    "add one contact to my contact book": add_contact,
    "display": display_contacts,
    "display contacts": display_contacts,
    "show": display_contacts,
    "show contacts": display_contacts,
    "remove": remove_contact,
    "remove contact": remove_contact,
    "remove a contact": remove_contact,
    "remove contacts": remove_contact,
    "remove contact from contact book": remove_contact,
    "remove a contact from contact book": remove_contact,
    "remove contacts from contact book": remove_contact,
    "remove a contact from my contact book": remove_contact,
    "remove contacts from my contact book": remove_contact,
    "remove one contact from my contact book": remove_contact,
    "remove from my contacts": remove_contact,
    "remove from my contacts book": remove_contact,
    "update": update_contact,
    "update contact": update_contact,
    "update a contact": update_contact,
    "update contacts": update_contact,
    "update contact in contact book": update_contact,
    "update a contact in contact book": update_contact,
    "update contacts in contact book": update_contact,
    "update a contact in my contact book": update_contact,
    "update contacts in my contact book": update_contact,
    "update one contact in my contact book": update_contact,
    "update from my contacts": update_contact,
    "update from my contacts book": update_contact,
    "filter": filter_contacts,
    "filter by": filter_contacts,
    "filter contacts": filter_contacts,
    "filter contact": filter_contacts,
    "filter a contact": filter_contacts,
    "filter a contact in contact book": filter_contacts,
    "filter contacts in contact book": filter_contacts,
    "filter a contact in my contact book": filter_contacts,
    "filter contacts in my contact book": filter_contacts,
    "filter one contact in my contact book": filter_contacts,
    "sort": sort_contacts,
    "sort by": sort_contacts,
    "sort contacts": sort_contacts,
    "sort contact": sort_contacts,
    "sort a contact": sort_contacts,
    "sort a contact in contact book": sort_contacts,
    "sort contacts in contact book": sort_contacts,
    "sort a contact in my contact book": sort_contacts,
    "sort contacts in my contact book": sort_contacts,
    "sort one contact in my contact book": sort_contacts
}
    
contacts = {} # This is the dictionary that acts as a contact book and stores all the contact objects as values to their corresponding phone number as a key. The dictionary will be added to once someone decideds to add a contact. THis dictionary is the data source that is effeected by all the functions e.g. add, display, remove, update, fiulter, sort contact

while True: # This is a while loop that will keep running until the user enters "exit" or "quit"
    user_input = input("Enter a command (or 'exit' to quit): ") # This will prompt the user to enter a command or exit/quit the program
    if user_input.lower() == "exit" or user_input.lower() == "quit": # This checks if the user wants to exit or quit the program. If they do, then the program will break the loop and exit the program.
        print("Exiting the program. Goodbye!") # This will print a message to the user that the program is exiting and they are being returned to the main menu
        break # This will break the loop and exit the program
    elif user_input.lower() in commands.keys(): # This checks whether the user has entered a valid command from any of the commands listed as key values in the commands dictionary
        commands[user_input.lower()](contacts)
    else:
        print("Please enter a valid command.")


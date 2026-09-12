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

def add_contact(contacts):

    # Step 1: get and validate phone number
# Adding a program that checks whether the phone number is valid or not. A valid phone number is one that has digits only and has 15 or fewer digits 

    while True: # This is a while loop that will keep running until the user enters a valid phone number
        phone_number = input("Enter a phone number: ") # This will prompt the user to enter a phone number#
        if phone_number.isdigit() and len(phone_number) <= 15: # This checks if the phone number is valid by checking if it contains only digits and has 15 or fewer digits
            break # If the phone number is valid, the loop will break and the program will continue
        else: # If the phone number is not valid, the program will print an error message and the loop will continue
            print("Invalid phone number. Please try again.") # This will print an error message if the phone number is not valid
# Step 2: check for duplicate phone number
        # Checking for whether the phone number given is already in the contact book or not. If it is, then the program will print an error message and ask the user to enter a different phone number. If it is not, then the program will continue and create a new contact with the given information.
    
    if phone_number in contacts: # This checks if the phone number is already in the contact book
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
    while True: # This is a while loop that will keep running until the user enters a valid phone number
        phone_number = input("Enter the phone number of the contact you want to remove: ") # This will prompt the user to enter the phone number of the contact they want to remove
        if phone_number.lower() == "cancel" or phone_number.lower() == "exit": # This checks if the user wants to cancel or exit the program. If they do, then the program will return to the main menu and not remove any contacts.
            print("Removing contact operation cancelled. Returning to main menu.") # This will print a message to the user that the operation has been cancelled and they are being returned to the main menu
            return # This will return to the main menu and not remove any contacts
        if phone_number.isdigit() and len(phone_number) <= 15: # This checks if the phone number is valid by checking if it contains only digits and has 15 or fewer digits
            break # If the phone number is valid, the loop will break and the program will continue
        else: # If the phone number is not valid, the program will print an error message and the loop will continue
            print("Invalid phone number. Please try again.") # This will print an error message if the phone number is not valid
    
    if phone_number in contacts: # This checks if the phone number is already in the contact book
        removed_contact = contacts.pop(phone_number) # This will remove the contact object by finding the phone number in the contact book and deleting it from the dictionary
        print(f"Contact removed: {removed_contact.first_name} {removed_contact.last_name}") # This will print the first name and last name of the contact removed and show the user
    else: # If the phone number is not in the contact book, then the program will print an error message and ask the user to enter a different phone number.
        print("This phone number doesn't exist in the contact book. Please enter a different phone number") # This will print an error message if the phone number is not in the contact book
Bwe
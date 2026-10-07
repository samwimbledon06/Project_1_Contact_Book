from contact import add_contact, display_contacts, contacts, Contact, valid_field_names # This whole google form look to use add_contact needs to have users input their answers into a google like form and then add_contact actually running on the back of this, therefore will need to add thye add_contact() function in this python file which is from the contact.py python fdile under the same folder
import tkinter as tk # This is the library tghat contains the Graphical User Interface that we will use to create a google-like form asking the user to input their contact details if add_contact is called. Giving the Tkinter library alias tk

print(contacts) # Temporary debugging line

root = tk.Tk() # Assigning the window or GUI that contains no buttons or fields as of yet ands is currently empty
# Adding first name to the form

first_name_label = tk.Label(root, text="First Name") # Creates a label with "First Name" and attaches it to the root
first_name_input = tk.Entry(root) # Creates a free text box beneath "First Name" widget to allow users to type their first name into

first_name_label.grid(row=0, column=0) # This is called on the widget itself so it actually appears in the window. The label "First Name" is in the first column and row of the pop up window so right in the top left
first_name_input.grid(row=0, column=1) # This widget appears just below the "First Name" widget itself when the pop window is shown. This widget is placed as a box to the right (right next to) the first name label where the user can free type in their first name

# Adding last name to the form

last_name_label = tk.Label(root, text="Last Name") # Creates a label with "Last Name" and attaches it to the root
last_name_input = tk.Entry(root) # Creates an empty text entry box, attached to the root, for the user to type their last name into

last_name_label.grid(row=1, column=0) # Places the label in the second row (row 1), first column (column 0)
last_name_input.grid(row=1, column=1) # Places the entry box in the second row (row 1), second column (column 1), right next to its matching label

# Adding email to the form

email_label = tk.Label(root, text="Email") # Creates a label with "email" and attaches it to the root
email_input = tk.Entry(root) # Creates an empty text entry box, attached to the root, for the user to type their email into

email_label.grid(row=2, column=0) # Places the label in the third row (row 2), first column (column 0)
email_input.grid(row=2, column=1) # Places the entry box in the third row (row 2), second column (column 1), right next to its matching label

# Adding country code to the form

country_code_label = tk.Label(root, text="Country code") # Creates a label with "country code" and attaches it to the root
country_code_input = tk.Entry(root) # Creates an empty text entry box, attached to the root, for the user to type their country_code into

country_code_label.grid(row=3, column=0) # Places the label in the fourth row (row 3), first column (column 0)
country_code_input.grid(row=3, column=1) # Places the entry box in the fourth row (row 3), second column (column 1), right next to its matching label

# Adding phone number to the form

phone_number_label = tk.Label(root, text="Phone number") # Creates a label with "phone number" and attaches it to the root
phone_number_input = tk.Entry(root) # Creates an empty text entry box, attached to the root, for the user to type their phone_number into

phone_number_label.grid(row=4, column=0) # Places the label in the fifth row (row 4), first column (column 0)
phone_number_input.grid(row=4, column=1) # Places the entry box in the fifth row (row 4), second column (column 1), right next to its matching label

# Adding city to the form

city_label = tk.Label(root, text="City") # Creates a label with "city" and attaches it to the root
city_input = tk.Entry(root) # Creates an empty text entry box, attached to the root, for the user to type their city into

city_label.grid(row=5, column=0) # Places the label in the sixth row (row 5), first column (column 0)
city_input.grid(row=5, column=1) # Places the entry box in the sixth row (row 5), second column (column 1), right next to its matching label

# Adding a submit button that when pressed, will trigger add_contacts() to run

submit_button = tk.Button(root, text="Submit", command=lambda: gui_add_contact(contacts))
# The Button widget's command= only accepts a function reference that tkinter can call later with ZERO arguments of its own —
# it decides when to call it (on click), not us, so we can't just write add_contact(contacts) directly here,
# since that would call add_contact immediately, right when the button is created.
# The lambda solves this: "lambda: add_contact(contacts)" creates a small, temporary function that takes no
# parameters itself (nothing between "lambda" and ":"), but when tkinter finally calls it (on click),
# it runs add_contact(contacts) internally — with contacts already "baked in" from this surrounding code.
submit_button.grid(row=6, column=1) # This submit label is palced in the 7th row (row 6) and attaches to the root


# Creating an error button 

error_label = tk.Label(root, text = "") # For now no error label should appear unless an invalid value is entered into a field
error_label.grid(row=7, column=0) # Places the error label in the 8th row (row 7) and attaches it to the roo

def gui_add_contact(contacts): # This function represents add_contacts(0 function but specifically for when a user inputs their add contact details using the GUI tkinter form presented to them
    first_name = first_name_input.get() # Retreiving the user input from first name using .get()
    last_name = last_name_input.get() # Retreiving the user input from last name using .get()
    email = email_input.get() # Retreiving the user input from email using .get()
    country_code = country_code_input.get() # Retreiving the user input from country code using .get()
    phone_number = phone_number_input.get() # Retreiving the user input from phone number using .get()
    city = city_input.get() # Retreiving the user input from city using .get()

    if phone_number.isdigit() and len(phone_number) <= 15: # Checks if phone number only contains digits and if the number of digits is 15 or less
        if phone_number in contacts: # Checks for if phone number already edxists, in which case, then this phone number would be a duplicate phone number which cant be accepted
            error_label.config(text = "This phone number already exists in our contacts book. Please enter a different phone number") # If a duplicate phone number then the GUI will throw an error message saying that the phone number already exists and prompt you to enter another phone number that is unique
            return # Stops fubnction from continuing

        else: # This block runs if phone number contains digits only and has 15 or less digits and is a unique phone number that doesnt exist in the contact book already
            if email.count("@") == 1 and email[0] != "@" and email[-1] != "@": # This checks if the email address is valid by checking if it contains exactly one "@" symbol and that the first and last characters are not "@" symbols
                if len(country_code) > 0 and country_code[0] == "+": # This checks whether there is more than one character and if the first character of the country code is a "+" symbol or not. If it is, then the program will continue and create a new contact with the given information. If it is not, then the program will print an error message and ask the user to enter a different country code.
                    country_code = country_code.strip("+") # This will remove the "+" symbol from the country code if it is present

                if country_code.isdigit(): # This checks whether the country code is made of just numbers or not. If it is, then the program will continue and create a new contact with the given information. If it is not, then the program will print an error message and ask the user to enter a different country code. If it is then all field name values entered are valid, so the contacts object is ready to be created
                    user_contact = Contact(first_name, last_name, email, country_code, phone_number, city) # This will create a new contact with the given information
                    contacts[phone_number] = user_contact # This will add the new contact to the contact book with the phone number as the key and the contact object as the value
                    display_contacts(contacts) # TEMPORARY - to just check contacts dictionary is populating correctly, remove once confirmed
                    error_label.config(text = "") # This ensures the error label returns back to its defauilt an empty string, so no error label shows
                    first_name_input.delete(0, tk.END) # delete the first all the way to the end of the characters that user inputted for first_name 
                    last_name_input.delete(0, tk.END) # delete the first all the way to the end of the characters that user inputted for last_name
                    email_input.delete(0, tk.END) # delete the first all the way to the end of the characters that user inputted for email
                    country_code_input.delete(0, tk.END) # delete the first all the way to the end of the characters that user inputted for country_code
                    phone_number_input.delete(0, tk.END) # delete the first all the way to the end of the characters that user inputted for phone number
                    city_input.delete(0, tk.END) # delete the first all the way to the end of the characters that user inputted for city

                else: # Only runs if country code doesnt contain only digits
                    error_label.config(text = "Please enter a valid country code containing only digits") # Throws an error message toi the GUI telling user to enter a valid country code
                    return # execution of function stops immediately after
            else: # This code block runs if email address is invalidly entered. Either because there is no @ symbol, more than one @ symbol or the 1 @ symbol is at the start or end character of the email address
                error_label.config(text = "Please enter a valid email address with an @ symbol.") # Throws an error message toi the GUI telling user to enter a valid email address
                return
    else: # if the phone number either doesnt contain just digits or has 16 or more digits
        error_label.config(text = "Please enter a valid phone number. A phone number must contain only digits and be 15 or less digits long.") # If an invalid phone number then the GUI will throw an error message asking the user to enter a vali correcly formatted phone number
        return # Stops fucntion from proceeding, exits function
    
root.mainloop() # command that starts the event loop - this will make window appear and stay open waiting for user to type and will run continuously instead of immediately closing
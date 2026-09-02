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
        
# Contact Book

A command-line contact book built in Python. This was my first Python project using classes and dictionaries together, and my first project developed with Git version control from the start.

## Features

- **Add a contact** — with validation for phone number, email, and country code, plus duplicate detection based on phone number
- **View all contacts**
- **Remove a contact**
- **Update a contact** — choose which field to update, including special handling for phone number changes (since it's used as the dictionary key)
- **Filter contacts** — search by any field and value (e.g. find everyone in a specific city)
- **Sort contacts** — sort by any field, in ascending or descending order
- Natural-language commands — type things like `add`, `add a contact`, or `add contact to contact book` and they all work
- Cancel/exit option available at almost every prompt, so you're never stuck partway through an operation

## How it works

- Each contact is stored as an instance of a `Contact` class (first name, last name, email, country code, phone number, city)
- All contacts are stored in a dictionary, keyed by phone number, so lookups and duplicate checks are fast
- A single `commands` dictionary maps typed phrases to the function that handles them, so the main menu loop stays simple no matter how many phrases are supported

## Running it

Make sure you have Python 3 installed, then run:

```bash
python contact.py
```

You'll be prompted to type a command (e.g. `add`, `view`, `delete`, `update`, `filter`, `sort`, `exit`) and the program will guide you from there.

## What I learned

This project was built step by step, with a focus on understanding *why* something works, not just copying code that works. Some highlights:
- Classes and object-oriented basics (`__init__`, `__str__`, attributes vs methods)
- Dictionaries as a lookup structure, and choosing the right key for fast, meaningful lookups
- Input validation and defensive coding (handling edge cases like empty strings, `KeyError`, duplicate data)
- Refactoring for DRY (Don't Repeat Yourself) — pulling repeated logic into shared helper functions once the shape of the whole project was clear
- Using Git properly from day one: small, descriptive commits building up a real project history

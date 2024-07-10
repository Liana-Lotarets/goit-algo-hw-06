from collections import UserDict

# Base class for record fields.
class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

# A class for storing a contact name. 
class Name(Field):
	pass

# A class for storing a phone number.
class Phone(Field):
    def __init__(self, value):
        # The class has format validation (10 digits).
        if len(value) == 10:
            super().__init__(value)
        else:
            print('Must be 10 digits.')
            self.value = ''        

# A class for storing contact information, including name and phone list.
class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones: list[Phone] = []

    # Adding a phone.
    def add_phone(self, phone: str):
        self.phones.append(Phone(phone))

    # Deleting a phone.
    def remove_phone(self, phone: str):
        self.phones.remove(Phone(phone))

    # Editing a phone.
    def edit_phone(self, old_number: str, new_number: str):
        try:
            # We are looking for a number that needs to be changed.
            for phone in self.phones:
                if phone.value == old_number:
                     old_number = phone
                     break
            # Get the index of the phone of the list "self.phones".
            old_number_index = self.phones.index(old_number)
        except ValueError as excpt:
             print(f'The phone cannot be edited. Incorrect input data: {excpt}')
        else:
            # Change the phone.
            self.phones[old_number_index] = Phone(new_number)

    # Phone search.
    def find_phone(self, wanted_phone: str):
        # We are looking for a phone.
        for phone in self.phones:
                if phone.value == wanted_phone:
                     wanted_phone = phone
                     break
        return wanted_phone if wanted_phone in self.phones else None

    # Magic method of beautiful output.
    def __str__(self):
        return f'Contact name: {self.name.value}, ' + \
            f'phones: {'; '.join(phone.value for phone in self.phones)}'

# A class for storing and managing records.
class AddressBook(UserDict):
    # Adding a record.
    def add_record(self, record: Record):
        self.data[record.name.value] = record

    # Search a record by name.
    def find(self, wanted_name: str):
        result = [self.data[key] for key in self.data \
                  if self.data[key].name.value == Record(wanted_name).name.value]
        return result[0] if len(result) != 0 else None
    
    # Deleting a record by name.
    def delete(self, name: str):
        self.data.pop(Record(name).name.value)

    # Magic method of beautiful output.
    def __str__(self):
        result = 'Address Book\n'
        for note in self.data.values():
             result += (f'  Contact name: {note.name.value}, '
             f'phones: {'; '.join(phone.value for phone in note.phones)}\n')
        return result.strip()
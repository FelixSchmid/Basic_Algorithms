class Phone_number:

    def __init__(self, number_type, number):
        self.number_type = number_type
        self.number = number

    def print(self):
        print(self.number_type + ': ' + self.number)

class Student:

    def __init__(self, firstname, lastname, birthday, email):
        self.firstname = firstname
        self.lastname = lastname
        self.birthday = birthday
        self.email = email
        

    def name(self):
        return self.firstname + ' ' + self.lastname

    def print(self):
        print(self.name())
        print(self.birthday)
        print(self.email)
        print(testnumber.number)
        

testnumber = Phone_number('Mobil', '0176 96116882')
felix = Student('Felix', 'Schmid', '21.10.93', 'felix.schmid@hotmail.de')

felix.print()
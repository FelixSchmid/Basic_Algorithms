
class Student:      
    
    def __init__(self, firstname, lastname, birthday, email, grade):
        self.firstname = firstname
        self.lastname = lastname
        self.birthday = birthday
        self.email = email
        self.phone = []
        self.grade = grade
    
    def add_phone(self, phonetype, phonenumber):
        self.phone.append(Phone(phonetype, phonenumber))

    def print(self):      
        output = self.firstname + " " + self.lastname + "\n" 
        output += "Birthday: " + self.birthday + "\n" 
        output += "Email: " + self.email + "\n" 
        output += "Grade: " + self.grade + "\n" 
        for number in self.phone:
            output += "Phone: " + str(number) + "\n"
        print(output)
        
class Phone:
    def __init__(self, phonetype, phonenumber):
        self.phonetype = phonetype
        self.phonenumber = phonenumber

    def __str__(self):
        return str(self.phonenumber) + " " + "(" + self.phonetype + ")"
        
felix = Student('Felix', 'Schmid', '21.10.93', 'felix.schmid@hotmail.de', '1.0')
felix.add_phone('mobile', '017696116882')
felix.print()
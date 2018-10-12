class Student:

    def __init__(self, firstname, lastname, birthday, grade):
        self.firstname = firstname
        self.lastname  = lastname
        self.birthday = birthday
        self.grade = grade   

felix = Student('Felix', 'Schmid', '21.10.93', '1')

print(felix)